# Day 25: Unsupervised Learning - K-Means Clustering

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Sample data
X = np.array([
    [1, 2],
    [1.5, 1.8],
    [5, 8],
    [8, 8],
    [1, 0.6],
    [9, 11]
])

# Create KMeans model
kmeans = KMeans(n_clusters=2, random_state=42)

# Fit model
kmeans.fit(X)

# Predict clusters
labels = kmeans.predict(X)

# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Means Clustering")
plt.show()
