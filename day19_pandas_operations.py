# Day 19: Pandas Data Cleaning & Operations

import pandas as pd
import numpy as np

# Create DataFrame with missing values
data = {
    "Name": ["Jashnavi", "Anu", "Ravi", "Kiran"],
    "Marks": [85, np.nan, 78, 92],
    "Age": [19, 20, np.nan, 21]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("--------------------")

# Fill missing values
df["Marks"].fillna(df["Marks"].mean(), inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)

print("After filling missing values:")
print(df)

print("--------------------")

# Add new column
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print("After adding Result column:")
print(df)

print("--------------------")

# Filter data
print("Students with Marks > 80:")
print(df[df["Marks"] > 80])
