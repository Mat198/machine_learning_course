#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(min_samples_split = 40)

print(features_test)

train_dataset_size = len(features_train)
print("Training data set size is", train_dataset_size, ".")

print("Data has", len(features_test[0]), "features!")

t0 = time()
clf.fit(features_train, labels_train)
print("Training Time:", round(time()-t0, 3), "s")

t0 = time()
score = clf.score(features_test, labels_test)
print("Predicting Time:", round(time()-t0, 3), "s")

print("Classifier score is", round(score, 3))

