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

In order to run this code, convert the `business_sample.json` dataset to a .csv with dummy variables, using the `dataset_json_to_csv2.csv` file. This will create a new .csv dataset, named `business_sample_csv.csv` with dummy variable attributes that can be used in your models.

After running the `dataset_json_to_csv2.csv` file, run the `runme.py` file in your terminal. This will gather accuracy scores and confusion matrixes from the csv dataset and save them to a dataset named `runme_prediction_csv.csv`. You will gather 10 accuracy scores and confusion matrixes. To view the confusion matrixes, I saved them in a text file, which can be seen in `runme_regression_results_text`. This is an optional step.

Following the `runme.py` file, which is a RandomForest model, run the `run_linear_regression.py` file in your terminal. This is a logistic regression model that will also gather accuracy scores and save them to a .csv file named `linear_regression_prediction_csv`.

Now, you will be able to see the accuracy scores from a logistic mdoel and a RandomForest model. My RandomForest model proved to be more accurate, so I used this to predict my review count.
- In the RandomForest model, you will see two for loops. This is meant to run the accuracy scores for multiple values of the classifier n_estimator and max_depth. In the .csv file, you will see the accuracy scores for each combination of classifier chosen. You can then choose the most accurate combination of classifier for your prediction model.

Following this, convert `business_no_stars_review.json` dataset to a .csv by running the `dataset_no_stars_to_csv.py` file, which will save the new dataset with dummy variables as `business_no_stars_review_csv.csv`. Run the code `runme_prediction.py` in your terminal to recieve the predicted review count stars for this dataset. These predicted stars will save under a dataset named `runme_stars_prediction_csv.csv`. 

# Customization of Code

Each of these codes are customizable, first starting with converting the datasets to a .csv file. In my code, I only converted a few attributes to dummy variables to usein my model code. These datasets contain many attributes which would help increase your accuracy scores in your prediction. Follow the same logic in my `dataset_json_to_csv2` code. For example, if you wanted to find all business with an attribute Apparel, you could add code which looks something like this:
```
	if cell_categories is not None:
		cell_apparel = ('Apparel' in cell_categories)
		if cell_apparel is not None:
			data_apparel.append(0)
		else: 
			data_apparel.append(1)
	else:
		data_apparel.append(2)
```
- Remember to add `data_apparel = []` at the beginning of your code and `'Apparel': data_apparel` in the DataFrame at the end of your code.

Once you add an attribute dummy variable to your dataset, you can amend your `runme.py` and `run_linear_regression` codes by adding that new variable column into your `data = dataset.iloc[].values` code. Your code will then use that column as an addition to run the model. 

# Files Explained
| Name | Description |
| --- | --- |
| dataset_json_to_csv2.csv | converts orignial dataset to a .csv dataset |
| runme.py | Runs a RandomForest model on the new `dataset_json_to_csv2` dataset to determine the accuracy scores and confusion matrix of the new .csv dataset |
| runme_prediction_csv.csv | Shows the accuracy scores of the runme.py file |
| runme_regression_results_text | Shows the combined accuracy scores and confusion matrix of the runme.py file |
| run_linear_regression.py | Runs a Logistic Regression model on the new `dataset_json_to_csv2` dataset to determine the accuracy scores of the new .csv dataset |
| linear_regression_prediction_csv.csv | Shows the accuracy scores of the run_linear_regression.py file |
| dataset_no_stars_to_csv | Converts the dataset which contains no review stars to a .csv file |
| runme_prediction | Runs a RandomForest model to predict the review stars on the dataset obtained by `dataset_no_stars_to_csv` file |

