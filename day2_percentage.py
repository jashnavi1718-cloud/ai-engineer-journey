# Day 2: Python Input and Output

name = input("Enter your name:S Jashnavi ")
marks1 = int(input("Enter marks of subject 1:Maths "))
marks2 = int(input("Enter marks of subject 2:Science "))
marks3 = int(input("Enter marks of subject 3:Social "))

total = marks1 + marks2 + marks3
percentage = (total / 300) * 100

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
