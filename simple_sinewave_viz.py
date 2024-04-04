import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Title and sidebar
st.title('A Scatter Plot')
st.sidebar.header('User Input')

# Generate random data
np.random.seed(0)
n_points = st.sidebar.slider('Number of points', 10, 1000, 50)
amp = st.sidebar.slider('Amplitude', 1.0, 10.0, 1.0)
x = np.random.rand(n_points)
y = amp*np.sin(2*np.pi*x)
data = pd.DataFrame({'x': x, 'y': y})

# Create a scatter plot based on user input
st.write('Scatter Plot based on User Input')

scatter_chart = alt.Chart(data).mark_circle().encode(
    x='x',
    y=alt.Y('y', scale=alt.Scale(domain=[-10, 10]))
).interactive()

# Display
st.write(scatter_chart)
st.write('Data modified from User Input')
st.write(data)
