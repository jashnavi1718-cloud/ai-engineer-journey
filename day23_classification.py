# Day 23: Supervised Learning - Classification (Logistic Regression)

from sklearn.linear_model import LogisticRegression
import numpy as np

# Training data (hours studied vs pass/fail)
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([0, 0, 0, 1, 1, 1])  # 0 = Fail, 1 = Pass

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[4]])
probability = model.predict_proba([[4]])

print("Prediction for 4 hours study:", "Pass" if prediction[0] == 1 else "Fail")
print("Prediction probability:", probability)
