# Sharpening my Machine Learning knowledge day by day
This repo will contain all of the things that I will learn during my MLxDaysChallenge.

## Day 1
- I began the [tutorial](https://www.analyticsvidhya.com/blog/2020/01/build-your-first-machine-learning-pipeline-using-scikit-learn/?utm_source=feedburner) about Machine Learning pipeline using BigMart Sales dataset from Analytics Vidhya.
- I stopped at Model Building.  

**ToC:** 
1. Understanding Problem Statement
2. Building a prototype model
    1. Data Exploration and Preprocessing
        1. Impute the missing values
        2. Encode the categorical variables
        3. Normalize/Scale the data if required
    2. Model Building
    3. Identifying features to predict the target
3. Designing the ML Pipeline using the best model
4. Predict the target on the unseen data.
  
## Day 2
- I finished the remaining parts of the Pipeline tutorial and submitted the results to get an idea about the model performance.
- I learned from this lesson that it's best to do a thorough analysis and towards the end, after building and choosing your model, you can cleverly define your pipeline.

## Day 3
- I have been curious about data science workflows and development cycle so I checked this amazing article: 
[Creating reproducible data science workflows with DVC](https://medium.com/y-data-stories/creating-reproducible-data-science-workflows-with-dvc-3bf058e9797b).
You will find it detailed in Data Science Workflows, and it's about data version control. I only did the first part and will finish it the following day. 

## Day 4
- I have finished the last tutorial about *Creating reproducible data science workflows with DVC*. While running the tutorial I have run into several problems due to the fact that I was runing all the commands in jupyter notebook. I witched to cmd and retook the 2nd part but there where still some things that didn't run as supposed (I am talking about the updating features part).
- I will be diving deeper into this DVC topic later on, to understand it more.

## Day 5 & 6

**Note**: I have decided that if a tutorial took me more than one day I will concatenate the days and write one review (because I like to spend only a specific time to keep the momentum going :) ).

- This tutorial was amazing because it is one of the few that goes from EDA to Model Evaluation. I learned a lot of things about how to deal with features especially the categorical ones (I like the fact that he tries to encode categories logically with numbers and not just call get_dummies).

## Day 7 & 8 & 9 & 10
- For the 1st day I worked on visualization to try to understand my data to make better decisions.
- The 2nd day I worked on cleaning and preprocessing the data to make it easier for the model to interpret.
- The 3rd day I began working on hyperparameter tuning (it actually took me 2 days because of the internet connection going down, I had to reduce the number of parameters as well).
- The 4th and last day (which is the day I am writing this), I submitted the first result (by leaving only 31 features) and I got 64% in ROC while testing on private data. I tried increasing the number of features to 50 it got worse and I changed the number of features to 20 and it got better.  
**C/c**:   
Perhaps trying other models will give a better result like : CatBoost, XGBoost and some other models.
I am not going to be trying more because I want to explore the solution that I got the best score and learn from it.

## Day 11 & 12
While preparing for my talk for IWD2020 organized by my community WTM Casablanca, I read and discovered about how to explain ML predictions to gain user's trust.  
Check the Ml explainability + trust.md file for more information on what I learned.
