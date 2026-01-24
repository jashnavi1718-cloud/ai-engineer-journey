# Day 13: Object Oriented Programming (OOP)

class Student:
    def __init__(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year

    def display_details(self):
        print("Student Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)


# Create object
student1 = Student("Jashnavi", "CSE (AI & ML)", 2)

# Call method
student1.display_details()
