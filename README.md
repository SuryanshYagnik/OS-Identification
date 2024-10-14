# Operating System Identification using Machine Learning and Deep Learning

This project aims to classify the operating system of a device based on network data using multiple machine learning and deep learning models: **Random Forest**, **Support Vector Machine (SVM)**, **Logistic Regression**, **Convolutional Neural Network (CNN)**, and **Recurrent Neural Network (RNN)**.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Model Breakdown](#model-breakdown)
    - [Random Forest](#random-forest)
    - [Support Vector Machine (SVM)](#support-vector-machine-svm)
    - [Logistic Regression](#logistic-regression)
    - [Convolutional Neural Network (CNN)](#convolutional-neural-network-cnn)
    - [Recurrent Neural Network (RNN)](#recurrent-neural-network-rnn)
- [Evaluation](#evaluation)
- [Dataset](#dataset)

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-directory>

## Usage

1. Ensure your dataset is in the correct format (`network_data.csv` or another format) where:

   - `X`: Features (the network data)
   - `y`: Target labels (OS identification)

2. To run the models, navigate to the appropriate script (e.g., `random_forest.py`, `cnn.py`).

3. For each model, the workflow is broken into 3 parts:
   - **Model Definition**
   - **Training**
   - **Evaluation**

---

## Model Breakdown

### Random Forest

To use the Random Forest model, run:

```bash
python random_forest.py
