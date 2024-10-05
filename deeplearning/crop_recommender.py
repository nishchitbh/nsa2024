import numpy as np
import joblib

# Load the saved model
loaded_model = joblib.load('randomforest_model.pkl')


def predict(data: list):
    # Prepare the data (replace these values with your input)
    data_to_predict = data

    # Convert the data to a 2D array (1 row, number of features columns)
    data_to_predict = np.array(data_to_predict).reshape(1, -1)

    # Make predictions
    predictions = loaded_model.predict(data_to_predict)

    # Print the predictions
    return "Predicted value:", predictions[0]
