# Day 6: Lists and Tuples

# List example
fruits = ["apple", "banana", "mango", "orange"]

print("Fruits list:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Add item to list
fruits.append("grapes")
print("After adding an item:", fruits)

# Remove item from list
fruits.remove("banana")
print("After removing an item:", fruits)

print("--------------------")

# Loop through list
print("Fruits using loop:")
for fruit in fruits:
    print(fruit)

print("--------------------")

# Tuple example
colors = ("red", "green", "blue")

print("Colors tuple:", colors)
print("First color:", colors[0])

# Tuple is immutable (cannot be changed)
