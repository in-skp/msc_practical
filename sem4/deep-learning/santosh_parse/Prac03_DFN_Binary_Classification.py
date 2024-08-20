from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import keras
from keras import layers
from keras import models
import pandas as pd
names = ["No.of pregnancies", " Glucose level", " Blood Pressure",
         "Skin Thickness", "Insulin", "BMI", "Diabetes Pedigree", "Age", "Class"]
df = pd.read_csv("data/diabetes.csv")
df.head()
# create  model
binaryc = models.Sequential()
# create layers in model or NN
binaryc.add(layers.Dense(units=10, activation="relu", input_dim=8))
binaryc.add(layers.Dense(units=8, activation="relu"))
binaryc.add(layers.Dense(units=1, activation="sigmoid"))
binaryc.compile(loss='binary_crossentropy',
                optimizer='adam', metrics=['accuracy'])
x = df.iloc[:, :-1]
y = df.iloc[:, -1]
xtrain, xtest, ytrain, ytest = train_test_split(
    x, y, test_size=0.25, random_state=1)
xtrain.shape
ytrain.shape
binaryc.fit(xtrain, ytrain, epochs=200, batch_size=20)
predict = binaryc.predict(xtest)
predict.shape
# binary classification
class_label = []
for i in predict:
    if (i >= 0.5):
        class_label.append(1)
    else:
        class_label.append(0)
# print accuracy score
print("Accuracy:", accuracy_score(ytest, class_label))
