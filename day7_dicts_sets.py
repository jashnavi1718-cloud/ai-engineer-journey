# Day 7: Dictionaries and Sets

# Dictionary example
student = {
    "name": "Jashnavi",
    "branch": "CSE (AI & ML)",
    "year": 2
}

print("Student details:")
print("Name:", student["name"])
print("Branch:", student["branch"])
print("Year:", student["year"])

# Add new key-value pair
student["college"] = "Kuppam Engineering College"
print("Updated dictionary:", student)

print("--------------------")

# Loop through dictionary
print("Dictionary keys and values:")
for key, value in student.items():
    print(key, ":", value)

print("--------------------")

# Set example
numbers = {1, 2, 3, 4, 4, 5}

print("Set values (no duplicates):", numbers)

# Add element to set
numbers.add(6)
print("After adding an element:", numbers)
