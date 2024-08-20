import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import keras
from keras import models
from keras import layers
from scikeras.wrappers import KerasRegressor
dataframe = pd.read_csv("data/housing.csv", sep=',', header=0)
print("Shape of dataset:", dataframe.shape)
print("First few rows of dataset:")
print(dataframe.head())
# Features (all columns except 'MEDV')
X = dataframe.drop(columns=['MEDV']).values
Y = dataframe['MEDV'].values  # Target variable ('MEDV')
print("Shape of X (features):", X.shape)


def wider_model():
    model = models.Sequential()
    model.add(
        layers.Dense(15, input_dim=X.shape[1], kernel_initializer='normal', activation='relu'))
    model.add(layers.Dense(13, kernel_initializer='normal', activation='relu'))
    model.add(layers.Dense(1, kernel_initializer='normal'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(
    build_fn=wider_model, epochs=5, batch_size=5)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=2, shuffle=True, random_state=42)
try:
    results = cross_val_score(pipeline, X, Y, cv=kfold,
                              scoring='neg_mean_squared_error')
    print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std()))
except ValueError as e:
    print("Error during cross-validation:", e)
