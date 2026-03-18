# Convolutional Neural Networks (CNN) – Computer Vision Fundamentals

This repository explains how Convolutional Neural Networks process images and learn visual patterns for tasks such as image classification, object detection, and facial recognition.

---

# Computer Vision

Computer Vision is a field of Artificial Intelligence that enables computers to interpret and understand visual information from images and videos.

## Image Processing

Image processing performs mathematical operations on images to extract useful features and improve visual quality.

---

# Biological Inspiration of CNN

CNN architecture is inspired by the **human visual cortex**, where neurons process visual signals in hierarchical layers.

## Visual Cortex

The visual cortex in the brain processes images through multiple layers that detect edges, shapes, and objects.

---

# Image Representation in CNN

Images are converted into numerical matrices before being processed by neural networks.

## Pixel Representation

Each pixel in an image is represented by numerical intensity values.

## Grayscale Image

Grayscale images are represented as **2D arrays of pixel values**.

## Colored Image

Color images are represented as **3D arrays containing RGB channels**.

---

# CNN Architecture

CNN models consist of multiple layers that progressively extract meaningful features from images.

## Convolution Layer

The convolution layer applies filters to detect features such as edges, textures, and shapes.

## Feature Map

The output of the convolution operation is called a **feature map**, which highlights detected patterns.

---

# Kernel / Filter

A kernel (or filter) is a small matrix that slides over the input image to extract features.

## Sliding Window Operation

The filter moves across the image and performs element-wise multiplication with pixel values.

---

# Stride

Stride defines how many pixels the filter moves at each step during convolution.

## Stride = 1

The filter moves one pixel at a time.

## Stride > 1

Larger stride reduces the size of the output feature map.

---

# Padding

Padding adds extra pixels around the image borders to control output dimensions.

## Valid Padding

No padding is applied and output size decreases.

## Same Padding

Padding is applied so output size remains similar to input.

---

# Activation Function

Activation functions introduce non-linearity into the network.

## ReLU (Rectified Linear Unit)

ReLU activates neurons only when input values are positive.

---

# Pooling Layer

Pooling reduces the spatial dimensions of feature maps while preserving important features.

## Max Pooling

Max pooling selects the largest value from a pooling window.

## Average Pooling

Average pooling computes the mean value of the window.

---

# Flattening Layer

Flattening converts 2D feature maps into a 1D vector before passing them to dense layers.

---

# Fully Connected Layer

Fully connected layers perform classification based on extracted features.

---

# CNN Processing Pipeline

Image → Convolution → Activation → Pooling → Flattening → Fully Connected Layer → Output.

---

# Example CNN Workflow

A digit image (like the number 8) is converted into pixel values and processed by CNN layers to recognize the digit.

---

# Feature Hierarchy in CNN

Lower layers detect edges while deeper layers detect complex patterns like shapes and objects.

---

# CNN Applications

CNNs are widely used in image-based Artificial Intelligence systems.

## Image Classification

Classifies objects such as animals, vehicles, or handwritten digits.

## Facial Recognition

Identifies individuals using facial features.

## Medical Imaging

Detects diseases in X-rays, MRI scans, and CT images.

## Autonomous Vehicles

Helps self-driving cars detect roads, pedestrians, and traffic signals.

## Emotion Recognition

Classifies facial expressions such as happy or sad.

---

# CNN vs Traditional Neural Networks

Traditional neural networks cannot efficiently handle images due to high dimensionality, while CNNs use convolution and pooling to extract spatial features efficiently.

---

# Learning Outcome

This project builds a strong understanding of image representation, convolution operations, CNN architecture, and computer vision applications.