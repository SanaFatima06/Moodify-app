# Moodify - Mood Based Song Recommender

Moodify is a machine learning web application that predicts the mood of a user based on text input and recommends songs accordingly.

## Features

- Predicts mood from user text input
- Uses a trained machine learning model (Logistic Regression + TF-IDF)
- Recommends top songs based on predicted mood
- Simple Flask-based web interface

## Tech Stack

- Python
- Flask
- Scikit-learn
- HTML
- Bootstrap
- Joblib

## How It Works

1. User enters a text input describing their feeling
2. The text is cleaned using preprocessing techniques
3. A trained ML model predicts the mood
4. Songs are recommended based on the predicted mood

## Installation

```bash
pip install -r requirements.txt
