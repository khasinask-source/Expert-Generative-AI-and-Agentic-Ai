# OpenCV Computer Vision Projects – Object Detection using Haar Cascade

This repository demonstrates basic computer vision applications using OpenCV including face detection, eye detection, car detection, pedestrian detection, and image processing.

---

# What is OpenCV

OpenCV (Open Source Computer Vision Library) is a powerful library used for real-time image processing, computer vision, and machine learning applications.

---

# Haar Cascade Classifier

Haar Cascade is a machine learning based object detection algorithm used to identify objects such as faces, eyes, cars, and pedestrians in images or videos.

---

# Image Processing Basics

Computer vision systems first convert images into numerical arrays so that algorithms can analyze patterns and features.

## Reading an Image

`cv2.imread()` loads an image from disk into a matrix format.

## Displaying an Image

`cv2.imshow()` displays the image in a window.

## Saving an Image

`cv2.imwrite()` saves processed images to disk.

---

# Image Preprocessing

Before detection, images are converted to grayscale to reduce computational complexity.

## Grayscale Conversion

`cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)` converts colored images into grayscale format.

---

# Face Detection using Haar Cascade

Face detection identifies human faces in an image by scanning different regions using trained cascade classifiers.

## Loading Face Classifier

`cv2.CascadeClassifier()` loads the pretrained Haar cascade XML file.

## Detecting Faces

`detectMultiScale()` scans the image and detects faces based on trained features.

## Drawing Bounding Box

`cv2.rectangle()` draws rectangles around detected faces.

---

# Face and Eye Detection

This program detects both faces and eyes in an image or video frame.

## Region of Interest (ROI)

After detecting a face, the algorithm searches for eyes within the face region.

## Eye Detection

Eye cascade classifiers detect eyes inside the face bounding box.

---

# Real-Time Face Detection (Webcam)

OpenCV can capture frames directly from the webcam and perform detection in real time.

## Video Capture

`cv2.VideoCapture(0)` opens the system webcam.

## Frame Processing

Each frame is converted to grayscale and passed through the face detection algorithm.

---

# Object Detection in Video

Haar cascade classifiers can also detect objects in videos frame-by-frame.

---

# Car Detection System

This project detects moving cars in video footage using a trained Haar cascade classifier.

## Car Detection Model

A trained XML classifier identifies car patterns in grayscale frames.

## Detection Process

Each frame of the video is processed and bounding boxes are drawn around detected vehicles.

---

# Pedestrian Detection

Pedestrian detection identifies people walking in video footage using full-body Haar cascade models.

## Body Classifier

`haarcascade_fullbody.xml` is used to detect full human body silhouettes.

## Detection Workflow

Video frames are processed sequentially and rectangles are drawn around detected pedestrians.

---

# Face and Eye Detection using Class Structure

An object-oriented implementation encapsulates face and eye detection logic inside a Python class.

## Initialization

The constructor loads face and eye cascade classifiers.

## Face Detection Method

A method scans grayscale frames and identifies face coordinates.

## Eye Detection Method

Eyes are detected within the face region to improve accuracy.

---

# Multi-Object Detection

Multiple faces and eyes can be detected simultaneously in a single frame.

---

# Computer Vision Pipeline

Image/Video Input → Grayscale Conversion → Haar Cascade Detection → Bounding Box Visualization → Output Display.

---

# Example Applications

These projects demonstrate real-world computer vision applications.

## Security Systems

Face detection for surveillance cameras.

## Driver Monitoring Systems

Eye detection to monitor driver attention.

## Smart Traffic Monitoring

Vehicle detection for traffic analysis.

## Pedestrian Safety Systems

Detecting pedestrians for autonomous vehicles.

---

# Learning Outcome

This project provides hands-on experience with:

* OpenCV image processing
* Haar cascade classifiers
* Face and eye detection
* Real-time webcam processing
* Vehicle and pedestrian detection
* Basic computer vision pipeline
