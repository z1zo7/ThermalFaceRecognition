# ThermalFaceRec: Face Recognition Using Thermal Imaging

## Overview

This project is a **Face Recognition System** utilizing **Thermal Imaging** for improved accuracy in low-light conditions. It leverages **Deep Learning** techniques with **Convolutional Neural Networks (CNNs)** to identify individuals based on thermal facial features.

## Features

- **Thermal Image Processing** for face recognition
- **Graphical User Interface (GUI)** for easy interaction
- **Database Integration** for storing recognition history
- **Image Preprocessing** for enhanced model accuracy
- **CNN Model Training & Inference** for real-time recognition

## Project Structure

```
├── App.py              # Main application entry point
├── connect.py          # Handles database connection
├── test.py             # Model testing script
├── Window1.py          # Dashboard window
├── Window2.py          # Add image window
├── Window3.py          # History window
├── library.py          # Helper functions and utilities
├── test model.h5       # Pre-trained Keras model
└── Final Doc.pdf       # Project documentation
```

## Cloning the Repository

To clone this repository, run the following command:

```bash
git clone https://github.com/MohamedAmr51/ThermalFaceRec.git
```

## Installation & Setup

### Prerequisites

- Python 3.7+
- Required Libraries:
  ```bash
  pip install pandas numpy matplotlib os glob cv2 keras tensorflow inference_sdk
  ```

Make sure you have Python installed on your system. If you don't have it, you can download it from [python.org](https://www.python.org/).

### Running the Application

1. Open the `App.py` file in your preferred IDE or text editor.
2. Run the file. You can do this by navigating to the directory containing `App.py` and executing the following command in your terminal:
   ```bash
   python App.py
   ```

## Image Format

Ensure that all images used for the thermal face recognition are in **BMP format**. Other image formats are not supported.

## Supported Platforms

This project has been tested and is supported on the following platforms:

- **VS Code** version 1.90.2
- **PyCharm** version 2023.2.5

## System Specifications

The program was tested and ran on a system with the following specifications:

- **CPU:** AMD Ryzen 4800H
- **GPU:** GTX 1650Ti (4GB)
- **RAM:** 16 GB

## Model Details

- This project uses the **YOLOv8** pre-trained model, specifically trained on thermal face datasets, to detect faces accurately in thermal images.

- The model (`test model.h5`) is a **CNN-based architecture** trained on thermal face images.

- Preprocessing includes **cropping, resizing, and normalization**.

- Predictions are made using **Keras and TensorFlow**.

## Contributions

Feel free to contribute to this project by opening issues or submitting pull requests.

## License

This project is for educational purposes and is open for modifications and enhancements.

