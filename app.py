import streamlit as st
import pandas as pd
import os
from six.moves import urllib
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder

download_dir = "./data/"

download_url = "https://raw.githubusercontent.com/aravind9722/datasets-for-ML-projects/main/cardekho_dataset.csv"

os.makedirs(download_dir,exist_ok=True)

filename = os.path.basename(download_url)

download_file_path = os.path.join(download_dir, filename)

urllib.request.urlretrieve(download_url, download_file_path)

df = pd.read_csv(download_file_path, index_col=[0])

model_file_path = "regressor.pkl" 

with open(model_file_path, "rb") as model_file:
   trained_model = pickle.load(model_file)

# Title and Introduction
st.title('Used Car Price Prediction')
st.write('This app predicts the selling price of used cars in India.')

# Sidebar Inputs
st.sidebar.header('User Input Features')

# Create inputs for each feature (use appropriate data types and ranges)

car_name = st.sidebar.selectbox('car_name', df['car_name'].unique())
brand = st.sidebar.selectbox('Brand', df['brand'].unique())
model = st.sidebar.selectbox('model', df['model'].unique())
vehicle_age = st.sidebar.slider('Vehicle Age', 1, 20, 5)
km_driven = st.sidebar.slider('Kilometers Driven', 500, 300000, 30000)
seller_type = st.sidebar.selectbox('Seller Type', df['seller_type'].unique())
fuel_type = st.sidebar.selectbox('Fuel Type', df['fuel_type'].unique())
transmission_type = st.sidebar.selectbox('Transmission Type', df['transmission_type'].unique())
mileage = st.sidebar.slider('Mileage (kmpl)', 5, 40, 15)
engine = st.sidebar.slider('Engine Capacity (cc)', 500, 5000, 1500)
max_power = st.sidebar.slider('Maximum Power (bhp)', 50, 400, 100)
seats = st.sidebar.slider('Number of Seats', 2, 10, 5)

# Load label encoders and scaler
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Preprocess the user inputs
# Preprocess the user inputs
user_input = pd.DataFrame({
    'car_name': [car_name],
    'brand': [brand],
    'model': [model],
    'vehicle_age': [vehicle_age],
    'km_driven': [km_driven],
    'seller_type': [seller_type],
    'fuel_type': [fuel_type],
    'transmission_type': [transmission_type],
    'mileage': [mileage],
    'engine': [engine],
    'max_power': [max_power],
    'seats': [seats],       
})

# Apply label encoding to categorical features
categorical_features = ['car_name', 'brand', 'model', 'seller_type', 'fuel_type', 'transmission_type']
for feature in categorical_features:
    le = label_encoders[feature]
    user_input[feature] = le.transform(user_input[feature])

# Ensure the order of columns matches the order used during training
user_input = user_input.reindex(columns=df.drop('selling_price', axis=1).columns)

# Apply standard scaling to numeric features
numeric_features = ['vehicle_age', 'km_driven', 'mileage', 'engine', 'max_power', 'seats']
user_input_scaled = scaler.transform(user_input[numeric_features])

# Combine label encoded categorical features and scaled numeric features
user_input_final = pd.concat([user_input[categorical_features], pd.DataFrame(user_input_scaled, columns=numeric_features)], axis=1)

# Reorder columns in user_input_final to match training column order
training_columns_order = df.columns.drop('selling_price')
user_input_final = user_input_final.reindex(columns=training_columns_order)


# Predict using the trained model
predicted_price = trained_model.predict(user_input_final)

# Display the predicted price
st.write('Predicted Used Car Price: INR', round(predicted_price[0], 2))

# Footer and Credits
st.write('App built by Your Name: Ayodele Ayodeji')

