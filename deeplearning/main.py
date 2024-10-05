import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load data from CSV
data = pd.read_csv('data.csv')

# Feature columns (excluding 'Soil Moisture' which is the target)
features = data[['Total Evapotranspiration', 'area under spi range', 'min tempr', 'max tempr', 'rainfall', 'accumulated rainfall']]

# Target column ('Soil Moisture')
target = data['Soil Moisture']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Normalize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),  # Input layer
    tf.keras.layers.Dense(128, activation='relu'),  # Hidden layer
    tf.keras.layers.Dense(64, activation='relu'),  # Hidden layer
    tf.keras.layers.Dense(1)  # Output layer (regression, no activation)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
history = model.fit(X_train_scaled, y_train, epochs=100, validation_data=(X_test_scaled, y_test))

# Evaluate the model on the test set
loss = model.evaluate(X_test_scaled, y_test)
print(f"Test loss: {loss}")

# Predict soil moisture on new data
predictions = model.predict(X_test_scaled)
