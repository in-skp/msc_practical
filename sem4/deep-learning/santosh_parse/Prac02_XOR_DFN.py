from keras import models
from keras import layers
import keras
import numpy as np
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
model = models.Sequential()
model.add(layers.Dense(units=2, activation='relu', input_dim=2))
model.add(layers.Dense(units=1, activation='sigmoid'))
print(model.get_weights())
x = np.array([[0., 0.], [0., 1.], [1., 0.], [1., 1.]])
y = np.array([0., 1., 1., 0.])
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])
model.fit(x, y, epochs=10, batch_size=4)
print(model.get_weights())
print(model.predict(x, batch_size=4))
print(model.summary)
