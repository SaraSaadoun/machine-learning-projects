import pandas as pd
import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load the KMeans model
with open('kmeans_model.pkl', 'rb') as file:
    kmeans = pickle.load(file)

# Set up the Streamlit interface
st.title("Mall Customer Clustering")

# Input fields for customer data
gender = st.selectbox("Gender", options=["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Annual Income (k$)", min_value=0, max_value=200, value=50)
spending_score = st.number_input("Spending Score (1-100)", min_value=1, max_value=100, value=50)

# Convert gender to numerical values
gender_num = 1 if gender == "Male" else 0

# Make prediction
if st.button("Predict Cluster"):
    features = np.array([[gender_num, age, income, spending_score]])
    cluster = kmeans.predict(features)

    # Display the predicted cluster
    st.success(f'The customer belongs to Cluster {int(cluster[0]) + 1}')
    
    # Cluster characteristics
    cluster_characteristics = {
        0: "Cluster 1: Young adults, budget-conscious with high spending tendencies.",
        1: "Cluster 2: Middle-aged customers with stable income and moderate spending.",
        2: "Cluster 3: Older professionals with high income but low spending.",
        3: "Cluster 4: Individuals enjoying luxury and high spending.",
        4: "Cluster 5: Older individuals or lower-income customers focused on value."
    }

    # Display characteristics of the predicted cluster
    st.subheader("Cluster Characteristics")
    st.write(cluster_characteristics[int(cluster[0])])
