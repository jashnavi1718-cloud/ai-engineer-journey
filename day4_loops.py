# Day 4: Python Loops Practice

# Task 1: Print numbers from 1 to 10 using for loop
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

print("\n----------------------\n")

# Task 2: Multiplication table of a given number
num = int(input("Enter a number for multiplication table: "))

print(f"\nMultiplication Table of {num}:")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("\n----------------------\n")

# Task 3: Sum of numbers from 1 to n using while loop
n = int(input("Enter a number to find sum: "))

total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("Sum of numbers from 1 to", n, "is:", total)
