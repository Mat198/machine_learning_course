#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()

# AdaBoost
from sklearn.ensemble import AdaBoostClassifier
from time import time

clf = AdaBoostClassifier(n_estimators=20, random_state=0, learning_rate=2.0)
t0 = time()
clf.fit(features_train, labels_train)

print("AdaBoos Classifier")
print("Training Time:", round(time()-t0, 3), "s")

t0 = time()
score = clf.score(features_test, labels_test)
print("Predicting Time:", round(time()-t0, 3), "s")

print("Classifier score is", round(score, 3))

try:
    prettyPicture(clf, features_test, labels_test, "adaboost.png")
except NameError:
    print("Failed to create dava visualization")
    pass
