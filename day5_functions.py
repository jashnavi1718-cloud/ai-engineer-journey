# Day 5: Python Functions

# Function 1: Greeting function
def greet():
    print("Hello!")
    print("Welcome to my AI Engineer journey 🚀")

greet()

print("--------------------")

# Function 2: Add two numbers
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)

print("--------------------")

# Function 3: Check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print("The number is", check_even_odd(number))
