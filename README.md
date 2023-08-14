# Indian Used Car Price Prediction Project

This project aims to predict the selling price of used cars based on various features in India. The project involves data preprocessing, feature selection, model training, and building an interactive web application using Streamlit.

## Table of Contents

- [Introduction](#introduction)
- [Data Preprocessing](#data-preprocessing)
- [Model Selection](#model-selection)
- [Streamlit Web App](#streamlit-web-app)
- [Getting Started](#getting-started)
- [Requirements](#requirements)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The used car market is vast and dynamic, and predicting the price of a used car accurately can be a valuable tool for both buyers and sellers. This project demonstrates the process of building a machine learning model to predict car prices based on various features such as vehicle age, kilometers driven, seller type, fuel type, and more.

## Data Preprocessing

The provided dataset was preprocessed to handle categorical variables using label encoding and feature scaling. Various algorithms were initially explored, including Linear Regression, Lasso, Ridge, K-Neighbors Regressor, Decision Tree, Random Forest Regressor, XGBRegressor, CatBoosting Regressor, and AdaBoost Regressor. After experimentation and evaluation, the Random Forest Regressor was selected as the final model due to its promising performance.

## Model Selection

The RandomForestRegressor from scikit-learn was chosen as the final model for car price prediction. This ensemble algorithm combines multiple decision trees to improve prediction accuracy and handle complex relationships in the data.

## Streamlit Web App

An interactive web application was developed using Streamlit to allow users to input car information and receive a predicted selling price. The app utilizes the trained Random Forest Regressor model to make predictions based on user inputs.

## Getting Started

To get started with the project, follow these steps:

1. Clone this repository to your local machine.
2. Install the required packages using the provided `requirements.txt` file.
3. Run the Streamlit app using the `app.py` file.

## Requirements

Install the required packages by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app by executing the following command:

```bash
streamlit run app.py
```

This will launch the app in your default web browser. Input the relevant car features, and the app will provide a predicted selling price.

## Contributing

Contributions to this project are welcome. Feel free to open issues, suggest improvements, or submit pull requests.