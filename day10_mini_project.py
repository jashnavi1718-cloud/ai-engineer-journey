# Day 10: Mini Project - Student Grade Calculator

print("Student Grade Calculator")

name = input("Enter student name: ")
marks = int(input("Enter marks (0-100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"

print("--------------------")
print("Student Name:", name)
print("Marks:", marks)
print("Grade:", grade)
