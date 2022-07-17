import cv2
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from PIL import Image
import PIL.ImageOps
import os, ssl, time
X = np.load('image.npz')['arr_0']
y = pd.read_csv('labels.csv')['labels']
print(pd.Series(y).value_counts())
classes = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nclasses = len(classes)
xTrain, xTest, yTrain, yTest = train_test_split(X, y, random_state = 9, train_size = 3500, test_size = 500)
xTrainScaled = xTrain / 255.0
xTestScaled = xTest / 255.0
clf = LogisticRegression(solver = 'saga', multi_class = 'multinomial').fit(xTrainScaled, yTrain)
yPred = clf.predict(xTestScaled)
accuracy = accuracy_score(yTest, yPred)
print('The accuracy is :-', accuracy)