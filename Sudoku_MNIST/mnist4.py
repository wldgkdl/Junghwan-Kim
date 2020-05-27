import tensorflow as tf
import numpy as np
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()



def train_images():
    return x_train

def train_labels():
    return y_train

def test_images():
    return x_test

def test_labels():
    return y_test
