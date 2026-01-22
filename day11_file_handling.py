# Day 11: File Handling in Python

# Write to a file
file = open("data.txt", "w")
file.write("Hello, this is Day 11 of my AI Engineer journey.\n")
file.write("Learning Python File Handling.\n")
file.close()

print("Data written to file successfully.")

print("--------------------")

# Read from the file
file = open("data.txt", "r")
content = file.read()
print("File content:")
print(content)
file.close()

print("--------------------")

# Append to the file
file = open("data.txt", "a")
file.write("Appending new data on Day 11.\n")
file.close()

print("Data appended successfully.")
