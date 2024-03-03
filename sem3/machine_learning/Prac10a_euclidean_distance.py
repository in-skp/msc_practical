from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv("data/IRIS.csv")
x = df.drop(['species'], axis=1)
y = df['species']
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=0)
knn = KNeighborsClassifier(n_neighbors=6, p=2, metric='minkowski')
knn.fit(x_train, y_train)
print(knn.score(x_test, y_test))
y_pred = knn.predict(x_test)
cm = np.array(confusion_matrix(y_test, y_pred))
print(cm)
knn = KNeighborsClassifier(n_neighbors=6, p=1, metric='minkowski')
knn.fit(x_train, y_train)
print(knn.score(x_test, y_test))
y_pred = knn.predict(x_test)
cm = np.array(confusion_matrix(y_test, y_pred))
print(cm)
knn = KNeighborsClassifier(n_neighbors=6, p=10000, metric='minkowski')
knn.fit(x_train, y_train)
print(knn.score(x_test, y_test))
y_pred = knn.predict(x_test)
cm = np.array(confusion_matrix(y_test, y_pred))
print(cm)
print("\n")
