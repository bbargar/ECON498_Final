from sklearn import linear_model
import pandas as pd
import kfold_template

dataset = pd.read_csv("business_sample_csv.csv")

print(dataset)

target = dataset.iloc[:,2].values
target = target.astype(int)
print(target)

data = dataset.iloc[:,[5,6,7,11,15]].values
print(data)

machine = linear_model.LogisticRegression()

accuracy_score, confusion_matrix = kfold_template.run_kfold(4, data, target, machine)

results = pd.DataFrame(['logistic ',accuracy_score])


results.to_csv('linear_regression_prediction_csv.csv')