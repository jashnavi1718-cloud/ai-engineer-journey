# Day 15: Polymorphism & Method Overriding

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


# Create objects
a = Animal()
d = Dog()
c = Cat()

# Call methods
a.speak()
d.speak()
c.speak()
