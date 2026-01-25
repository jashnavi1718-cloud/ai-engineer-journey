# Day 14: Inheritance in Python

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child class
class Student(Person):
    def __init__(self, name, age, branch):
        super().__init__(name, age)
        self.branch = branch

    def show_student_details(self):
        self.show_details()
        print("Branch:", self.branch)


# Create object
student1 = Student("Jashnavi", 19, "CSE (AI & ML)")
student1.show_student_details()
