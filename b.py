# class Dog:
#     species = "Canine" # class attribute

#     def __init__(self, name, age):
#         self.name = name # Instance attribute
#         self.age = age # Instance attribute

# #Create an object for the Dog class
# dog1 = Dog("Buddy", 3)

# print(dog1.name)
# print(dog1.species)

# class student:
#     def __init__(self, id, name, gender):
#         self.id = id
#         self.name = name
#         self.gender = gender
#     def __str__(self):
#         return (f"{self.id}, {self.name}, {self.gender}")
# s1 = student(1001, "Dara", "Male")
# print(s1)

# class Employee:

#     def __init__(self, id, name, position, salary):
#         self.id = id
#         self.name = name
#         self.position = position
#         self.salary = salary

#     def __str__(self):
#         return f"{self.id} | {self.name} | {self.position} | ${self.salary}"

# emp = Employee(1, "Davit", "Manager", 3000)

# print(emp)

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old."

# dog1 = Dog("Kyky", 3)
# dog2 = Dog("Lolo", 5)

# print(dog1)
# print(dog2)

# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#     def show(self):
#         print("Model: ", self.model)
#         print("Color: ", self.color)
# audi = Car("Audi A4", "Blue")
# ferrari = Car("Ferrari 488", "Green")

# audi.show()
# ferrari.show()

# class Student:
#     def __new__(cls, name):
#         print("1. __new__() is called")
#         instance = super().__new__(cls)
#         return instance
#     def __init__(self, name):
#         print("2. __init__() is called")
#         self.name = name
#     def show(self):
#         print("Name: ", self.name)

# s= Student("Dara")
# s.show()

# class Car:
#     def __init__(self):
#         self.make = "Toyota"
#         self.model = "Corolla"
#         self.year = 2020
# car = Car()
# print(car.make)
# print(car.model)
# print(car.year)

# class Calculator:
#     def multiply(self, a=1, b=1, *args):
#         result = a * b
#         for num in args:
#             result *= num
#         return result
# cal = Calculator()
# print(cal.multiply())
# print(cal.multiply(4))
# print(cal.multiply(2, 3))
# print(cal.multiply(2, 3, 4))

# class Animal:
#     def sound(self):
#         return "Some generic sound"
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
# animals = [Dog(), Cat(), Animal()]
# for animal in animals:
#     print(animal.sound())

# class Animal:
#     def eat(self):
#         print("Animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
# dog = Dog()
# dog.eat()
# dog.bark()

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         print(self.name, "is eating")
# class Dog(Animal):
#     pass
# dog = Dog("Buddy")
# print(dog.name)
# dog.eat()

# class Animal:
#     def __init__(self, name):
#         self.name = name
# class Dog(Animal):
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
# dog = Dog("Buddy", "Golden Retriever")
# print(dog.name)
# print(dog.breed)

class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
dog = Dog("Buddy", "Golden Retriever")
print(dog.name)
print(dog.breed)

class Animal:
    def __init__(self, name):
        self.name = name
    def info(self):
        print("Animal name:", self.name)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def details(self):
        print(self.name, "is a", self.breed)
d = Dog("Buddy", "Golden Retriever")
d.info()
d.details()