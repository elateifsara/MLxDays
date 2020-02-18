import argparse
import pathlib
import pandas as pd

def get_ps(pclass, sex):
    """Calculate `PclassSex` feature."""

    pclasssex = (pclass - 1)*2 + int(sex == "male")
    return pclasssex

def categorize(odir, trname, tsname):
    """Impute missing values."""

    # To get consistent categories, we concatenate train and test
    train = pd.read_csv(trname, index_col="PassengerId")
    test = pd.read_csv(tsname, index_col="PassengerId")
    df = pd.concat([train, test], sort=False)

    # Getting categorical features
    df["CabinId"] = df["Cabin"].str.get(0)
    df["CabinId"] = df["CabinId"].astype("category").cat.codes
    df["EmbarkedId"] = df["Embarked"].astype("category").cat.codes
    df["Sex"] = df["Sex"].astype("category").cat.codes
    df["PclassSex"] = df.apply(lambda x: get_ps(x.Pclass, x.Sex), axis=1)

    # Saving features
    cols = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch",
            "Fare", "CabinId", "EmbarkedId"]

    odir = pathlib.Path(odir)
    df.loc[train.index, cols].to_csv(odir.joinpath("train_features.csv"))
    df.loc[test.index, cols[1:]].to_csv(odir.joinpath("test_features.csv"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--out-dir", dest="odir",
                        required=True, help="output directory")
    parser.add_argument("-r", "--train", dest="trname",
                        required=True, help="training file")
    parser.add_argument("-s", "--test", dest="tsname",
                        required=True, help="test file")
    args = parser.parse_args()
    categorize(args.odir, args.trname, args.tsname)
