#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()

# KNN
from sklearn.neighbors import KNeighborsClassifier
from time import time

clf = KNeighborsClassifier(n_neighbors=10, weights='distance',p=2)
t0 = time()
clf.fit(features_train, labels_train)

print("KNN Classifier")
print("Training Time:", round(time()-t0, 3), "s")

t0 = time()
score = clf.score(features_test, labels_test)
print("Predicting Time:", round(time()-t0, 3), "s")

print("Classifier score is", round(score, 3))

try:
    prettyPicture(clf, features_test, labels_test, "knn.png")
except NameError:
    print("Failed to create dava visualization")
    pass
