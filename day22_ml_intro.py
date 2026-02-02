# Day 22: Introduction to Machine Learning - Linear Regression

from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # features
y = np.array([50, 55, 60, 65, 70])           # labels

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Prediction
prediction = model.predict([[6]])

print("Predicted value for input 6:", prediction[0])
