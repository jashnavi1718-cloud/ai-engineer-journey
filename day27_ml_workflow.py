# Day 27: End-to-End ML Workflow - Student Result Prediction

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Dataset: Hours studied vs Pass/Fail
X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y = np.array([0, 0, 0, 1, 1, 1, 1, 1])  # 0 = Fail, 1 = Pass

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model
model = LogisticRegression()

# Train
model.fit(X_train_scaled, y_train)

# Predict
y_pred = model.predict(X_test_scaled)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Predict new value
new_hours = [[6]]
new_hours_scaled = scaler.transform(new_hours)
prediction = model.predict(new_hours_scaled)

print("Prediction for 6 hours study:",
      "Pass" if prediction[0] == 1 else "Fail")
