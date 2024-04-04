# Iris Flower Prediction App

## Overview
This is a Streamlit-based web application that allows users to predict the species of an Iris flower based on its sepal length, sepal width, petal length, and petal width. The app uses a pre-trained machine learning model to make the predictions.

## Features
- User-friendly slider interface to input the Iris flower measurements
- Real-time prediction of the Iris flower species
- 
## Technologies Used
- Python
- Streamlit
- Scikit-learn (for the machine learning model)
- Pandas (for data manipulation)
- Matplotlib and Seaborn (for data visualization)

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Streamlit
- Scikit-learn
- Pandas
- Matplotlib
- Seaborn

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-username/iris-flower-prediction-app.git
   ```
2. Navigate to the project directory:
   ```
   cd iris-flower-prediction-app
   ```
3. Create a virtual environment (optional but recommended):
   ```
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the App
1. Start the Streamlit app:
   ```
   streamlit run app.py
   ```
2. The app will open in your default web browser. You can now input the Iris flower measurements and see the predicted species.

## Usage
1. Enter the sepal length, sepal width, petal length, and petal width of the Iris flower you want to predict.
2. Click the "Predict" button to see the predicted Iris flower species.
3. The app will also display a scatter plot of the input data and the predicted species.

## Contributing
If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
