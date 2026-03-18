# OpenCV Color Detection using HSV – Computer Vision Project

This repository demonstrates real-time color detection using OpenCV by converting webcam video frames into HSV color space and applying color masks to detect specific colors.

---

# Computer Vision Color Detection

Color detection is a computer vision technique used to identify objects based on their color properties in images or video streams.

---

# Video Capture using Webcam

The system captures real-time video from the webcam and processes each frame individually.

## Webcam Initialization

`cv2.VideoCapture(0)` opens the default system webcam.

## Frame Extraction

Each video frame is read continuously using `cap.read()`.

---

# Color Representation in OpenCV

OpenCV images are stored in **BGR color format** by default.

## BGR Color Space

BGR represents pixel colors using Blue, Green, and Red channels.

## HSV Color Space

HSV represents colors using Hue, Saturation, and Value which makes color detection easier.

---

# BGR to HSV Conversion

The captured frame is converted from BGR to HSV format.

## HSV Conversion

`cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)` converts the image to HSV color space.

---

# HSV Components

HSV color model separates color information from brightness.

## Hue

Represents the actual color (red, blue, green, etc.).

## Saturation

Represents how intense or pure the color is.

## Value

Represents brightness or light intensity.

---

# Color Masking

Color masks isolate specific colors in an image based on HSV value ranges.

## Creating HSV Range

A lower and upper HSV range defines the boundaries of the target color.

---

# Red Color Detection

Red objects are detected by creating a mask for the HSV range representing red.

## Red Mask

`cv2.inRange()` creates a binary mask where red pixels are white and others are black.

---

# Blue Color Detection

Blue objects are detected using a different HSV range.

## Blue Mask

The mask highlights blue-colored regions in the frame.

---

# Green Color Detection

Green objects are extracted using a green HSV threshold.

## Green Mask

The mask filters out only green colored pixels.

---

# Detecting All Colors Except White

A mask can be created to remove white background and keep other colors.

## Non-White Mask

The HSV range excludes white color pixels while keeping other colors.

---

# Bitwise Image Filtering

After creating the mask, the color region is extracted using bitwise operations.

## Bitwise AND Operation

`cv2.bitwise_and()` applies the mask to the original frame and keeps only selected color pixels.

---

# Real-Time Color Detection

The processed frames are displayed continuously in real time.

## Display Windows

`cv2.imshow()` shows original frames and filtered color results.

---

# Program Exit Condition

The program runs in a loop until the user presses the **ESC key**.

## Key Event

`cv2.waitKey()` listens for keyboard input to terminate the program.

---

# Computer Vision Processing Pipeline

Webcam Video → Frame Capture → BGR to HSV Conversion → Color Masking → Bitwise Filtering → Display Detected Colors.

---

# Applications of Color Detection

Real-time color detection has many real-world applications.

## Object Tracking

Detect colored objects such as balls, markers, or robots.

## Industrial Automation

Sort products on conveyor belts based on color.

## Traffic Monitoring

Detect traffic lights and colored signals.

## Augmented Reality

Track colored markers for interactive systems.

---

# Learning Outcome

This project provides practical experience with:

* OpenCV webcam processing
* BGR and HSV color spaces
* Color masking techniques
* Bitwise image operations
* Real-time computer vision systems
