import kfold_template

import pandas as pd 

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

import numpy as np 

import json

dataset = pd.read_csv('business_sample_csv.csv')


# print(dataset)



target = dataset.iloc[:,2].values
data = dataset.iloc[:,[5,6,7,11,15]].values 

target = target.astype(int)
# print(target)
#  print(data)
n_estimators_list = [5,10,20,30,40]
max_depth_list = [5,10,20,40,50]
results_list = []

for i in max_depth_list:
	machine = RandomForestClassifier(n_estimators=20, criterion='gini', max_depth=i, n_jobs=4)
	accuracy_score, confusion_matrix = kfold_template.run_kfold(4, data, target, machine)
	results_list.append(['gini ',accuracy_score,str(i),'n_estimators = 20'])
	print(accuracy_score)
	for i in confusion_matrix:
		print(i)

for j in n_estimators_list:
	machine = RandomForestClassifier(n_estimators=j, criterion='gini', max_depth=20, n_jobs=4)
	accuracy_score, confusion_matrix = kfold_template.run_kfold(4, data, target, machine)
	results_list.append(['gini ',accuracy_score,str(j),'max_depth_list = 20'])
	print(accuracy_score)
	for i in confusion_matrix:
		print(i)

results = pd.DataFrame(results_list)


results.to_csv('runme_prediction_csv.csv')
