from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('data/iris.csv')
print(df.head())
print(df.dtypes)
print(df['species'].value_counts())

x = df.drop(['species'], axis=1)
y = df['species']
print(x.shape)
print(y.shape)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=0)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

clf = SVC(kernel='linear').fit(x_train, y_train)
print(clf.predict(x_train))
y_pred = clf.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
cm_df = pd.DataFrame(cm, index=['SETOSA', 'VERSICOLR', 'VIRGINICA'], columns=[
                     'SETOSA', 'VERSICOLR', 'VIRGINICA'])

plt.figure(figsize=(5, 4))
sns.heatmap(cm_df, annot=True)
plt.title('Confusion Matrix')
plt.ylabel('Actual Values')
plt.xlabel('Predicted Values')
plt.show()
