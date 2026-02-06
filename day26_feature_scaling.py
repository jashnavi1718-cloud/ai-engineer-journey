# Day 26: Feature Scaling & Data Preprocessing

from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data (features with different scales)
X = np.array([
    [1, 200],
    [2, 300],
    [3, 400],
    [4, 500]
])

print("Original Data:")
print(X)

print("--------------------")

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Scaled Data:")
print(X_scaled)
