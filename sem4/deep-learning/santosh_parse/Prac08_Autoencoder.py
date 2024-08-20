import matplotlib.pyplot as plt
import keras
from keras import layers
from keras import datasets
import numpy as np
encoding_dim = 32
input_img = keras.Input(shape=(784,))
encoded = layers.Dense(encoding_dim, activation='relu')(input_img)
decoded = layers.Dense(784, activation='sigmoid')(encoded)
autoencoder = keras.Model(input_img, decoded)
encoder = keras.Model(input_img, encoded)
encoded_input = keras.Input(shape=(encoding_dim,))
decoder_layers = autoencoder.layers[-1]
decoder = keras.Model(encoded_input, decoder_layers(encoded_input))
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()
x_train.shape
x_test.shape
x_train = x_train.astype('float32')/255
x_test = x_test.astype('float32')/255
x_train[0]
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
x_train[0]
print(x_train.shape)
print(x_test.shape)
autoencoder.fit(x_train, x_train, epochs=50, batch_size=256,
                validation_data=(x_test, x_test))
encoded_imgs = encoder.predict(x_test)
decoded_imgs = decoder.predict(encoded_imgs)
n = 10
plt.figure(figsize=(40, 4))
for i in range(10):
    ax = plt.subplot(3, 20, i+1)
    plt.imshow(x_test[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax = plt.subplot(3, 20, i+1+20)
    plt.imshow(encoded_imgs[i].reshape(8, 4))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax = plt.subplot(3, 20, 2*20+i+1)
    plt.imshow(decoded_imgs[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()
