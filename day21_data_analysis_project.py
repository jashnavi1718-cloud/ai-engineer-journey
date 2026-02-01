# Day 21: Mini Data Analysis Project - Student Performance

import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Name": ["Jashnavi", "Anu", "Ravi", "Kiran", "Sita"],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("--------------------")

# Basic analysis
average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

print("--------------------")

# Visualization
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance Analysis")
plt.show()
