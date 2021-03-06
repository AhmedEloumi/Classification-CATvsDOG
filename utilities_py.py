# -*- coding: utf-8 -*-
"""utilities.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DUqEggAoC7xCP5B1X5kWQEJiW3sE3X5V
"""

import h5py
import numpy as np


def load_data():
    train_dataset = h5py.File('/content/trainset.hdf5', "r")
    X_train = np.array(train_dataset["X_train"][:]) # your train set features
    y_train = np.array(train_dataset["Y_train"][:]) # your train set labels

    test_dataset = h5py.File('/content/testset.hdf5', "r")
    X_test = np.array(test_dataset["X_test"][:]) # your train set features
    y_test = np.array(test_dataset["Y_test"][:]) # your train set labels
    train_dataset.close()
    test_dataset.close()


    return X_train, y_train, X_test, y_test

