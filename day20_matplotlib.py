# Day 20: Data Visualization using Matplotlib

import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5]
marks = [70, 75, 80, 85, 90]

# Line plot
plt.plot(days, marks)
plt.xlabel("Days")
plt.ylabel("Marks")
plt.title("Progress Over Days")
plt.show()

# Bar chart
names = ["Jashnavi", "Anu", "Ravi", "Kiran"]
scores = [85, 90, 78, 92]

plt.bar(names, scores)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Scores")
plt.show()
