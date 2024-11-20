#!/usr/bin/python3
import os
import joblib
import sys
import matplotlib.pyplot
sys.path.append(os.path.abspath("../tools/"))
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = joblib.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL")
data = featureFormat(data_dict, features)

max_salary = max(data[:,0])
print("Max salary", max_salary)
for key, value in data_dict.items():
    if (float(value["salary"]) > 1e6) and (float(value["bonus"]) > 5e6):
        print(key, "is a bandit!")

### your code below

import matplotlib.pyplot as plt
plt.scatter(data[:,0], data[:,1]) 
plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()

