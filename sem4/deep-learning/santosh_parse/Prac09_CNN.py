from keras import datasets
from keras import utils
from keras import models
from keras import layers
import matplotlib.pyplot as plt
# Download MNIST data and split into train and test sets
(X_train, Y_train), (X_test, Y_test) = datasets.mnist.load_data()
# Plot the first image in the dataset
plt.imshow(X_train[0])
plt.show()
print(X_train[0].shape)
# Reshape the input data
X_train = X_train.reshape(60000, 28, 28, 1)
X_test = X_test.reshape(10000, 28, 28, 1)
# One-hot encode the labels
Y_train = utils.to_categorical(Y_train)
Y_test = utils.to_categorical(Y_test)
print(Y_train[0])
# Create a Sequential model
model = models.Sequential()
# Add model layers
# Learn image features
model.add(layers.Conv2D(64, kernel_size=3,
          activation='relu', input_shape=(28, 28, 1)))
model.add(layers.Conv2D(32, kernel_size=3, activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(10, activation='softmax'))
# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['accuracy'])
# Train the model
model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=3)
# Predict and print the probabilities for the first 4 images in the test set
print(model.predict(X_test[:4]))
# Print the actual labels for comparison
print(Y_test[:4])
