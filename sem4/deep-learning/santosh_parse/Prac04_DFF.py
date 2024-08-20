import pandas as pd
import keras
from keras import layers
from keras import models
from sklearn.preprocessing import LabelEncoder
from keras import utils
import numpy as np
# Define column names
names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
# Read the CSV file skipping the first row
df = pd.read_csv("data/flowers.csv", names=names, skiprows=0)
# Extract features and target variable
X = df.iloc[:, :-1].astype(float)
y = df.iloc[:, -1]
# Encode the target variable
lb = LabelEncoder()
y = lb.fit_transform(y)
encoded_Y = utils.to_categorical(y)
# Build the model
model = models.Sequential()
model.add(layers.Dense(8, activation='relu', input_dim=4))
model.add(layers.Dense(6, activation='relu'))
model.add(layers.Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
# Train the model
model.fit(X, encoded_Y, epochs=100, batch_size=10)
# Make predictions
predictions = model.predict(X)
# Output predictions and actual values
for i in range(35, 130, 3):
    print(predictions[i], encoded_Y[i])
# Create a DataFrame to compare predictions and actual values
a = []
for i in range(0, 150):
    a.append(np.argmax(predictions[i]))
newdf = pd.DataFrame(list(zip(a, y)), columns=['A', 'Y'])
print(newdf)
