import numpy as np
import joblib
import os

# Load the saved model
model_path = os.path.join(os.getcwd(), 'deeplearning', 'randomforest_model.pkl')
loaded_model = joblib.load(model_path)


def predict(data):
    # Prepare the data (replace these values with your input)
    data_to_predict = data

    # Convert the data to a 2D array (1 row, number of features columns)
    data_to_predict = np.array(data_to_predict).reshape(1, -1)

    # Make predictions
    predictions = loaded_model.predict(data_to_predict)

    # Print the predictions
    return predictions[0]
