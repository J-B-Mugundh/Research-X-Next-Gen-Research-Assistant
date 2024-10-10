import os

import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from ml_utility import (read_data,
                        preprocess_data,
                        train_model,
                        evaluate_model)

# Get the working directory of the main.py file
working_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(working_dir)

st.set_page_config(
    page_title="Automate ML",
    page_icon="🧠",
    layout="centered")

st.title("🤖 No-Code ML Model Trainer")

dataset_list = os.listdir(f"{parent_dir}/data")

# Dropdown to select a dataset or upload a new dataset
dataset = st.selectbox("Select a dataset from the dropdown", dataset_list, index=None)
upload_button = st.button("Upload a dataset")

# Handle file upload
if upload_button:
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = read_data(uploaded_file)
        st.dataframe(df.head())
else:
    df = read_data(dataset)

if df is not None:
    st.dataframe(df.head())

    # Display target column selection
    st.subheader("Target Column Selection")
    target_column = st.selectbox("Select the Target Column", list(df.columns))

    # Display preprocessing options
    st.subheader("Preprocessing")
    scaler_type_list = ["standard", "minmax"]
    scaler_type = st.selectbox("Select a Scaler", scaler_type_list)

    # Display model selection
    st.subheader("Model Selection")
    model_dictionary = {
        "Logistic Regression": LogisticRegression(),
        "Support Vector Classifier": SVC(),
        "Random Forest Classifier": RandomForestClassifier(),
        "XGBoost Classifier": XGBClassifier()
    }
    selected_model = st.selectbox("Select a Model", list(model_dictionary.keys()))

    # Input for model name
    st.subheader("Model Name")
    model_name = st.text_input("Enter the model name")

    # Button to train the model
    if st.button("Train the Model"):

        st.button("Download the Model")  # Dummy button for download

        X_train, X_test, y_train, y_test = preprocess_data(df, target_column, scaler_type)

        model_to_be_trained = model_dictionary[selected_model]

        model = train_model(X_train, y_train, model_to_be_trained, model_name)

        accuracy = evaluate_model(model, X_test, y_test)

        st.success("Test Accuracy: " + str(accuracy))
