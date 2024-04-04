import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Sidebar title and user input
st.sidebar.title('Model Fitting App')
st.sidebar.write('Enter sample data points:')

# User input fields for sample data
data_points = st.sidebar.text_input('Enter data points separated by commas (e.g., 1,2,3,4,5)', '1,2,3,4,5')

# Check for empty input before processing
if data_points:
    X = np.array([float(x) for x in data_points.split(',') if x.strip()]).reshape(-1, 1)  # Feature (independent variable)
    y = np.array([2*x for x in X]).reshape(-1, 1)  # Target (dependent variable)

    # Initialize and fit a linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Display model parameters and predictions
    st.write('### Model Parameters:')
    st.write(f'Intercept (b0): {model.intercept_[0]}')
    st.write(f'Coefficient (b1): {model.coef_[0][0]}')

    # User input for new data points to predict
    new_data_points = st.text_input('Enter new data points to predict separated by commas', '6,7')
    
    if new_data_points:
        new_X = np.array([float(x) for x in new_data_points.split() if x.strip()]).reshape(-1, 1)

        # Predict using the fitted model
        predictions = model.predict(new_X)
        st.write('### Predictions for New Data:')
        for i in range(len(new_X)):
            st.write(f'Prediction for {new_X[i][0]}: {predictions[i][0]}')
    else:
        st.write('Please enter valid new data points.')
else:
    st.write('Please enter valid sample data points.')