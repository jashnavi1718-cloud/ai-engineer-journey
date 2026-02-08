# Day 28: Introduction to Deep Learning (Neural Network)

from sklearn.neural_network import MLPClassifier
import numpy as np

# Simple dataset
X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [6, 7],
    [7, 8],
    [8, 9]
])

y = np.array([0, 0, 0, 1, 1, 1])  # Binary output

# Create Neural Network model
model = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000, random_state=42)

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[5, 6]])

print("Prediction for input [5,6]:",
      "Class 1" if prediction[0] == 1 else "Class 0")
