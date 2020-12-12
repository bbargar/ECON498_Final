import pandas as pd 

from sklearn.ensemble import RandomForestClassifier

import json


dataset = pd.read_csv('business_sample_csv.csv')


target = dataset.iloc[:,2].values
data = dataset.iloc[:,[5,6,7,11,15]].values 
target = target.astype(int)

machine = RandomForestClassifier(n_estimators=20, criterion='gini', max_depth=40, n_jobs=4)
machine.fit(data, target)



new_dataset = pd.read_csv('business_no_stars_review_csv.csv')
new_data = new_dataset.iloc[:,[4,5,6,10,14]].values 

results = machine.predict(new_data)

print(results)


results_predict = pd.DataFrame(results)
results_predict.to_csv('runme_stars_prediction_csv.csv')