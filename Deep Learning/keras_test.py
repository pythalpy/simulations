print("hello wurld")

import numpy as np
np.random.seed(123)  # for reproducibility

""" Next, we’ll import the Sequential model type from Keras. This is simply a linear stack of neural network layers, 
and it’s perfect for the type of feed-forward CNN we’re building in this tutorial."""
from keras.models import Sequential

"""Next, let’s import the “core” layers from Keras. These are the layers that are used in almost any neural network:"""
from keras.layers import Dense, Dropout, Activation, Flatten

"""Then, we’ll import the CNN layers from Keras. These are the convolutional layers that will help us efficiently train 
on image data:"""
from keras.layers import Convolution2D, MaxPooling2D

"""Finally, we’ll import some utilities. This will help us transform our data later:"""
from keras.utils import np_utils


from keras.datasets import mnist

# Load pre-shuffled MNIST data into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()


from matplotlib import pyplot as plt
plt.imshow(X_train[0])

X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)



X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)


model = Sequential()