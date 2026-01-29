# Day 18: Pandas Basics

import pandas as pd

# Create a Series
marks = pd.Series([85, 90, 78, 92, 88])
print("Series:")
print(marks)

print("--------------------")

# Create a DataFrame
data = {
    "Name": ["Jashnavi", "Anu", "Ravi", "Kiran"],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("--------------------")

# Basic DataFrame operations
print("First 2 rows:")
print(df.head(2))

print("DataFrame shape:", df.shape)
print("Column names:", df.columns)
