from matplotlib import pyplot
from sklearn.datasets import make_moons
from keras import models
from keras import layers
X, Y = make_moons(n_samples=100, noise=0.2, random_state=1)
n_train = 30
trainX, testX = X[:n_train, :], X[n_train:]
trainY, testY = Y[:n_train], Y[n_train:]
model = models.Sequential()
model.add(layers.Dense(500, input_dim=2, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])
history = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=100)
pyplot.plot(history.history['accuracy'], label='train')
pyplot.plot(history.history['val_accuracy'], label='test')
pyplot.legend()
pyplot.show()
