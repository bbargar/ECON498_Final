# ECON498_Final

# Introduction
This code is meant to convert a .json dataset to .csv, then run a RandomForest model and Linear Regression model on the dataset, then use the RandomForest model to predict the review count stars.

# Installation
To install this code, run 'git clone https://github.com/bbargar/ECON498_Final.git' in your terminal.

Other codes needed for installation, run this code:

'python3 pip install numpy pandas sklearn'

# Code Progression
To understand this code's progression, it can be simply stated in four steps.

`STEP 1`: Convert all necessary datasets to .csv

`STEP 2`: Run a RandomForest model on the dataset

`STEP 3`: Run a Linear Regression model on the dataset

`STEP 4`: Choose the best trained model, amend and run a prediction model on the dataset to achieve the predicted review count stars.

In order to run this code, convert the `business_sample.json` dataset to a .csv with dummy variables, using the `dataset_json_to_csv2.csv` file. This will create a new .csv dataset with dummy variable attributes that can be used in your models.

After running the `dataset_json_to_csv2.csv` file, run the `runme.py` file in your terminal. This will gather accuracy scores and confusion matrixes from the csv dataset and save them to a dataset named `runme_prediction_csv.csv`. You will gather 10 accuracy scores and confusion matrixes. To view the confusion matrixes, I saved them in a text file, which can be seen in `runme_regression_results_text`. This is an optional step.

Following the `runme.py` file, which is a RandomForest model, run the `run_linear_regression.py` file in your terminal. This is a logistic regression model that will also gather accuracy scores and save them to a .csv file named `linear_regression_prediction_csv`.

Now, you will be able to see the accuracy scores from a logistic mdoel and a RandomForest model. My RandomForest model proved to be more accurate, so I used this to predict my review count.
- In the RandomForest model, you will see two for loops. This is meant to run the accuracy scores for multiple values of the classifier n_estimator and max_depth. In the .csv file, you will see the accuracy scores for each combination of classifier chosen. You can then choose the most accurate combination of classifier for your prediction model.

