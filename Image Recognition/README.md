# CIFAR-10 Image Classification with Convolutional Neural Network (CNN)

This project demonstrates image classification using a Convolutional Neural Network (CNN) on the CIFAR-10 dataset. The CIFAR-10 dataset consists of 60,000 32x32 color images in 10 classes, with 6,000 images per class. The classes are mutually exclusive and include:

- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

## Project Overview

This repository contains a Python script `cifar10_cnn.py` that performs the following tasks:

1. **Loading and Preprocessing the Dataset**: Loads the CIFAR-10 dataset using TensorFlow/Keras and preprocesses the images by normalizing pixel values to the range [0, 1].

2. **Defining the CNN Model**: Constructs a CNN model using TensorFlow's Keras API. The model architecture includes convolutional layers with ReLU activation, max pooling, dropout for regularization, and dense layers with softmax activation for classification.

3. **Training the Model**: Compiles the model with the Adam optimizer and categorical crossentropy loss function, and trains it on the training data for 10 epochs.

4. **Evaluating the Model**: Evaluates the trained model on the test data to compute test accuracy.

5. **Saving the Model**: Saves the trained model in HDF5 format (`cifar10_cnn_model.h5`) for future use.

6. **Making Predictions**: Provides a function to load the saved model and make predictions on new images.

## Requirements

- Python 3
- TensorFlow 2.x
- numpy

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mhmmeddanish/Image_Recognition.git
   cd cifar10-image-classification
