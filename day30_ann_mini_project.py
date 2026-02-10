# Day 30: ANN Mini Project - Student Pass Prediction

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Dataset: Hours studied & attendance
X = np.array([
    [2, 60],
    [3, 65],
    [4, 70],
    [5, 75],
    [6, 80],
    [7, 85],
    [8, 90]
])

y = np.array([0, 0, 0, 1, 1, 1, 1])  # 0 = Fail, 1 = Pass

# Build ANN model
model = Sequential([
    Dense(10, activation='relu', input_shape=(2,)),
    Dense(5, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(X, y, epochs=100, verbose=0)

# Predict
test_student = [[6, 78]]
prediction = model.predict(test_student)

print("Prediction value:", prediction)
print("Result:",
      "Pass" if prediction[0][0] > 0.5 else "Fail")
