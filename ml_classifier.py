import streamlit as st
from streamlit_space import space
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


st.title('An Iris Flower Prediction App')
st.write('This streamlit app predicts the iris flower species based on user inputs of its features.')

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Create a RandomForestClassifier model
clf = RandomForestClassifier()
clf.fit(X, y)
space(lines=1)

# Create input fields
sepal_length = st.slider('Sepal Length', 4.0, 8.0, 5.0)
sepal_width = st.slider('Sepal Width', 2.0, 4.5, 3.0)
petal_length = st.slider('Petal Length', 1.0, 7.0, 4.0)
petal_width = st.slider('Petal Width', 0.1, 2.5, 1.0)

# Make predictions
prediction = clf.predict([[sepal_length, sepal_width, petal_length, petal_width]])

# Display the prediction
species = iris.target_names[prediction][0]
space(lines=1)
st.header(f'**The predicted species is 🌱 "{species}"**', anchor=None)
space(lines=3)

st.header('Appendix')
space(lines=3)
st.write('ML Features Example')
space(lines=2)
st.write(pd.DataFrame(iris["data"], columns=iris["feature_names"]))
space(lines=5)
st.write('ML Targets')
space(lines=2)
st.write(iris["target_names"])



