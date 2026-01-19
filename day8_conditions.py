# Day 8: Conditional Statements

# Task 1: Check positive, negative or zero
num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

print("--------------------")

# Task 2: Check even or odd
number = int(input("Enter another number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("--------------------")

# Task 3: Find largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)
