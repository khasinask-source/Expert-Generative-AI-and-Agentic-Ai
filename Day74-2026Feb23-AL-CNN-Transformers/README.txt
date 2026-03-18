# Deep Learning & CNN Fundamentals – Keras Applications

This repository demonstrates practical Deep Learning workflows using Keras and TensorFlow for image preprocessing, data augmentation, and pretrained CNN model predictions.

## TensorFlow & Keras
TensorFlow provides the computational backend while Keras offers a high-level API for building and deploying deep learning models.

## Image Data Augmentation
Data augmentation artificially expands datasets by applying random transformations to improve model generalization.

## ImageDataGenerator
ImageDataGenerator dynamically generates modified image batches using transformations such as rotation, shifts, zoom, and flipping.

## Rotation Transformation
Rotation randomly rotates images to help models learn orientation-invariant features.

## Width & Height Shifts
Shift transformations move images horizontally or vertically to increase spatial robustness.

## Shear Transformation
Shearing distorts images geometrically to simulate viewpoint variations.

## Zoom Transformation
Zooming scales images in or out to improve scale-invariant learning.

## Horizontal Flipping
Horizontal flipping mirrors images to diversify training samples.

## Fill Modes
Fill modes define how missing pixels are handled after transformations.

## Image Loading
Images are loaded into memory for preprocessing and augmentation operations.

## img_to_array Conversion
Images are converted into NumPy arrays for numerical processing by neural networks.

## Batch Dimension Expansion
Input arrays are reshaped to include batch dimensions required by CNN models.

## Flow-Based Generation
The `.flow()` method continuously generates transformed image batches for visualization or training.

## Preview Image Creation
Augmented images are saved to directories to visually inspect transformation effects.

## Pretrained CNN Models
Keras Applications provide pretrained models trained on ImageNet for transfer learning and inference.

## ResNet50
ResNet50 uses residual connections to enable very deep networks without vanishing gradient issues.

## ResNet50V2
ResNet50V2 improves residual learning using refined normalization and activation ordering.

## VGG16
VGG16 uses deep stacks of small convolution filters for hierarchical feature extraction.

## VGG19
VGG19 extends VGG16 with additional layers for deeper representation learning.

## Xception
Xception applies depthwise separable convolutions for efficient feature learning.

## InceptionV3
InceptionV3 captures multi-scale features using parallel convolution branches.

## MobileNetV2
MobileNetV2 optimizes performance for lightweight and mobile-friendly deployments.

## DenseNet121
DenseNet121 connects layers densely to encourage feature reuse and reduce parameters.

## NASNetMobile
NASNetMobile is a neural architecture search-based efficient CNN for mobile devices.

## NASNetLarge
NASNetLarge is a high-capacity architecture discovered through automated search.

## EfficientNetV2
EfficientNetV2 balances depth, width, and resolution for optimized performance.

## Image Preprocessing
Images are resized and normalized to match model-specific input requirements.

## preprocess_input Function
Model-specific normalization aligns image pixel distributions with training conditions.

## Prediction Inference
Models generate probability distributions representing class likelihoods.

## decode_predictions
Predicted probabilities are mapped to human-readable ImageNet class labels.

## Top Class Identification
The most probable class index is extracted using argmax operations.

## Inference Time Measurement
Execution time is measured to evaluate model prediction efficiency.

## Model Size Estimation
Model memory footprint is approximated using parameter counts.

## Parameter Analysis
Total trainable parameters indicate model complexity.

## Model Depth
Model depth reflects the number of computational layers.

## Practical Learning Outcome
This project builds intuition for CNN preprocessing, augmentation strategies, pretrained architectures, and performance analysis.