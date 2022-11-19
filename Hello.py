import tensorflow as tf

import keras

import matplotlib.pyplot as plt



#Importing the image dataset

from keras.datasets import mnist

#Loaded data
#I love butt sex
# kill me and put my dick in my butt
(x_train, y_train), (x_test, y_test) = mnist.load_data()

plt.imshow(x_train[0])
plt.show()