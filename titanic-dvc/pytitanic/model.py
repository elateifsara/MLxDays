import argparse
import pathlib
import json
import numpy as np
import pandas as pd
from catboost import CatBoostClassifier
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import roc_auc_score, accuracy_score


def train(odir, trname, tsname, split_col, rs, train_size):
    """Train gradient boosting model."""

    # To get consistent categories, we concatenate train and test
    train = pd.read_csv(trname, index_col="PassengerId")
    test = pd.read_csv(tsname, index_col="PassengerId")

    fts_cols = train.columns.drop("Survived")

    # Creating training/validation split
    cv = StratifiedShuffleSplit(n_splits=1,
                                train_size=train_size,
                                random_state=rs)

    tridx, cvidx = list(cv.split(train, train[split_col]))[0]

    # Fill missing values
    train.fillna(train.iloc[tridx].mean()[["Age", "Fare"]],
                 inplace=True)
    test.fillna(train.iloc[tridx].mean()[["Age", "Fare"]],
                inplace=True)

    # Creating the model
    model = CatBoostClassifier(iterations=500,
                               depth=4, rsm=0.75,
                               learning_rate=0.001,
                               early_stopping_rounds=250,
                               random_state=rs,
                               use_best_model=True)
    model.fit(train.iloc[tridx][fts_cols],
              train.iloc[tridx]["Survived"],
              eval_set=(train.iloc[cvidx][fts_cols],
                        train.iloc[cvidx]["Survived"]),
              verbose=50)

    # Measuring performance
    cv_predictions = model.predict_proba(train.iloc[cvidx][fts_cols])[:, 1]

    auc = roc_auc_score(train.iloc[cvidx, 0], cv_predictions)
    acc = accuracy_score(train.iloc[cvidx, 0], cv_predictions > 0.5)

    # Saving the model, metrics file and submission
    odir = pathlib.Path(odir)

    model.save_model(odir.joinpath("cb-model.cbm").as_posix())

    with open(odir.joinpath("cb-metrics.json"), "w") as metrics_file:
        metrics_file.write(json.dumps({"AUC": auc, "Accuracy": acc}))

    submission = pd.Series(model.predict(test.values),
                           name="Survived",
                           index=test.index,
                           dtype=np.int)

    submission.to_csv(odir.joinpath("cb-submission.csv"), header=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--out-dir", dest="odir",
                        required=True, help="output directory")
    parser.add_argument("-r", "--train", dest="trname",
                        required=True, help="training file")
    parser.add_argument("-s", "--test", dest="tsname",
                        required=True, help="test file")
    parser.add_argument("--split-col", dest="split_col",
                        default="Pclass", help="column to stratify on")
    parser.add_argument("--rnd", dest="rs", type=int,
                        default=515, help="random state")
    parser.add_argument("--train-size", dest="train_size", type=float,
                        default=0.75, help="train size")

    args = parser.parse_args()
    train(args.odir, args.trname, args.tsname,
          args.split_col, args.rs, args.train_size)
