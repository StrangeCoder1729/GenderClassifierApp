# GenderClassifierApp

## Overview
GenderClassifierApp is a web application designed to predict gender based on facial features. It utilizes machine learning algorithms to analyze input data and provide predictions on whether the input corresponds to a man or a woman.

## Features
- **User-Friendly Interface**: Simple and intuitive web interface for inputting facial feature data.
- **Prediction Engine**: Uses a trained machine learning model to predict gender based on input parameters.
- **Interactive Feedback**: Instantaneous feedback on predictions displayed on the web interface.
- **Scalable**: Designed to handle multiple users simultaneously, ensuring robust performance.

## Music Credits
- **Song**: "Facts"
- **Artist**: Tom MacDonald (feat. Ben Shapiro)
- **YouTube Link**: [Facts - Tom MacDonald (feat. Ben Shapiro)](https://www.youtube.com/watch?v=5kGpohEpuTE)

## How It Works
- **Input**: Users provide facial feature data such as forehead width, nose characteristics, and other relevant attributes via a user-friendly form.
- **Processing**: The input data is processed by a pre-trained Random Forest model, which has been trained to classify gender based on these features.
- **Output**: The application outputs a prediction indicating whether the input data corresponds to a man or a woman.

## Technologies Used
- **Python**: Backend logic and machine learning model training.
- **Flask**: Web framework for handling HTTP requests and responses.
- **HTML/CSS**: Frontend design and user interface.
- **JavaScript**: Enhances interactivity and form handling on the client-side.
- **Scikit-learn**: Used for data preprocessing and machine learning model implementation.

## Usage

### Clone the repository
```bash
git clone <repository_url>
```
### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the Flask application
```bash
python app.py

Access the web application through the provided URL and interact with the prediction form.
```
