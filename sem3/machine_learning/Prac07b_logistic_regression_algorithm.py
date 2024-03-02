from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('data/DMVWrittenTests.csv')
X = dataset.iloc[:, [0, 1]].values
Y = dataset.iloc[:, 2].values
dataset.head(5)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.25, random_state=0)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = LogisticRegression()
classifier.fit(X_train, Y_train)

y_pred = classifier.predict(X_test)
print(y_pred)

cm = confusion_matrix(Y_test, y_pred)
print("Accuracy:", accuracy_score(Y_test, y_pred))
print(cm)
