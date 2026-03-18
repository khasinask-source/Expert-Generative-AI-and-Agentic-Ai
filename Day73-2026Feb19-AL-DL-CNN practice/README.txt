# Deep Learning using TensorFlow & Keras – ANN and CNN Projects

This repository demonstrates deep learning concepts including Artificial Neural Networks (ANN), Convolutional Neural Networks (CNN), and practical image classification projects using TensorFlow and Keras.

---

# What is Deep Learning

Deep Learning is a branch of Artificial Intelligence that enables machines to learn complex patterns from data using neural networks similar to the human brain.

## Neural Network Families

Deep learning models are typically built using different neural network architectures:

* Artificial Neural Network (ANN)
* Convolutional Neural Network (CNN)
* Recurrent Neural Network (RNN)

---

# Deep Learning Frameworks

Deep learning frameworks provide tools and infrastructure for building neural network models efficiently.

## TensorFlow

TensorFlow is an open-source deep learning framework used to build and train neural networks.

## Keras

Keras is a high-level neural network API that runs on top of TensorFlow and simplifies deep learning model development.

## PyTorch

PyTorch is another popular deep learning framework used for research and production.

## OpenCV

OpenCV is a computer vision library used for image processing and real-time vision applications.

---

# Neural Network Architecture

A neural network architecture consists of multiple layers that process data sequentially.

## Input Layer

The input layer receives the raw data such as images or numerical features.

## Hidden Layers

Hidden layers perform computations and extract patterns from the data.

## Output Layer

The output layer produces the final prediction or classification.

---

# Artificial Neural Network (ANN)

Artificial Neural Networks are machine learning models inspired by biological neurons.

## Artificial Neuron

Each neuron receives inputs, multiplies them with weights, and produces an output using an activation function.

## Signal Flow

Data flows from the input layer through hidden layers to the output layer.

---

# Forward Propagation

Forward propagation is the process where input data moves through the neural network from input layer to output layer.

---

# Backpropagation

Backpropagation is the process of adjusting weights by propagating prediction errors backward through the network.

---

# Activation Functions

Activation functions determine the output of a neuron and introduce non-linearity.

## Sigmoid

Sigmoid converts input values into probabilities between 0 and 1.

## ReLU (Rectified Linear Unit)

ReLU activates neurons only when input values are positive.

## Softmax

Softmax converts outputs into probability distributions for multi-class classification.

---

# Epoch

An epoch represents one complete forward and backward pass through the training dataset.

---

# Convolutional Neural Networks (CNN)

CNNs are specialized neural networks designed to process image data and extract spatial features.

---

# Image Representation in CNN

Images are converted into numerical matrices before being processed by CNN models.

## Grayscale Image

Represented as a 2-dimensional array of pixel values.

## Color Image

Represented as a 3-dimensional array containing Red, Green, and Blue channels.

---

# CNN Architecture

CNN models consist of several layers used for feature extraction and classification.

## Convolution Layer

Applies filters (kernels) to extract features such as edges, shapes, and textures.

## Kernel / Filter

A small matrix that slides across the image to detect patterns.

---

# Stride

Stride determines how many pixels the filter moves across the image during convolution.

---

# Padding

Padding adds extra pixels around the image to preserve spatial dimensions.

---

# Max Pooling

Max pooling reduces the size of feature maps by selecting the maximum value within a pooling window.

---

# Flatten Layer

Flattening converts multidimensional feature maps into a one-dimensional vector.

---

# Fully Connected Layer

Fully connected layers perform the final classification using extracted features.

---

# CNN Processing Pipeline

Image → Convolution → Activation → Pooling → Flatten → Fully Connected → Output.

---

# Project 1 – Customer Churn Prediction (ANN)

This project predicts whether a customer will leave a company based on historical banking data.

## Objective

Identify customers likely to stop using a product or service.

## Model

ANN model built using TensorFlow and Keras.

---

# Project 2 – Fashion MNIST Classification

Fashion MNIST is a dataset containing images of clothing items used for image classification tasks.

## Dataset

* 60,000 training images
* 10,000 testing images
* Image size: 28×28 grayscale

## Goal

Train a neural network to classify fashion products into 10 categories.

---

# Project 3 – Mood Classification (CNN)

This project classifies facial expressions into two categories: Happy and Sad.

## Dataset Structure

Dataset contains two folders:

* Happy
* Not Happy / Sad

Training, testing, and validation folders are used for model training.

---

# Image Data Generator

ImageDataGenerator is used to automatically load and preprocess images during training.

---

# CNN Model Architecture

The CNN model includes multiple convolution and pooling layers followed by dense layers.

Example architecture:

Conv2D → MaxPooling → Conv2D → MaxPooling → Conv2D → MaxPooling → Flatten → Dense → Output

---

# Model Compilation

The model is compiled using:

* Loss function: Binary Crossentropy
* Optimizer: RMSProp
* Metric: Accuracy

---

# Model Training

The model is trained for multiple epochs using the training dataset and validated using the validation dataset.

---

# Prediction

The trained model predicts whether an input image represents a happy or sad facial expression.

---

# Visualization

Training results can be visualized using accuracy and loss graphs.

---

# Learning Outcome

This project provides hands-on experience with:

* Neural network architecture
* CNN image processing
* TensorFlow and Keras implementation
* Image classification models
* Computer vision applications
