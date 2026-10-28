# # Super()
# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

# dog = Dog("Buddy", "Golden Retriever")
# print(dog.name)
# print(dog.breed)

# # Method  Overriding
# class Person:
#     def introduce(self):
#         return "I am a person."

# class Student(Person):
#     def introduce(self):
#         return "I am a student."

# class Teacher(Person):
#     def introduce(self):
#         return "I am a teacher."

# student = Student()
# student = Student()
# print(Student.introduce)
# print(Teacher.introduce)

# # Abstract
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# dog = Dog()
# cat = Cat()
# print(dog.sound())
# print(cat.sound())

# Calculate Area
# from abc import ABC, abstractmethod
# import math
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
# class Circle(Shape):
#     def __init__(self, redius):
#         self.redius = redius
#     def area(self):
#         return math.pi * self.redius * 2
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return 0.5 * self.base * self.height
# rectangle = Rectangle(10, 5)
# circle = Circle(5)
# triangle = Triangle(10, 5)
# print("Rectangle Area:", rectangle.area())
# print("Circle Area:", circle.area())
# print("Triangle Area:", triangle.area())

# System Payment
# from abc import ABC, abstractmethod
# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
# class ABA(Payment):
#     def pay(self, amount):
#         return f"Paid ${amount} using ABA."
# class ACLEDA(Payment):
#     def pay(self, amount):
#         return f"Paid ${amount} using ACLEDA."
# class Wing(Payment):
#     def pay(self, amount):
#         return f"Paid ${amount} using Wing."
# aba = ABA()
# ac = ACLEDA()
# wing = Wing()
# print(aba.pay(100))
# print(ac.pay(50))
# print(wing.pay(25))

# Employee Salary
# from abc import ABC, abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass
# class FullTimeEmployee(Employee):
#     def __init___(self, monthly_salary):
#         self.monthly_salary = monthly_salary
#     def calculate_salary(self):
#         return self.monthly_salary
# class PartTimeEmployee(Employee):
#     def __init__(self, hours, rate):
#         self.hour = hours
#         self.rate = rate
#     def calculate_salary(self):
#         return self.hours * self.rate
# fulltime = FullTimeEmployee(500)
# parttime = PartTimeEmployee(60,5)
# print("Full Time Salary:", fulltime.calculate_salary())
# print("Part Time Salary:", parttime.calculate_salary())

# from abc import ABC, abstractmethod
# class BankAccount(ABC):
#     @abstractmethod
#     def deposit(self, amount):
#         pass
#     def withdraw(self, amount):
#         pass
# class CurrentMoney(BankAccount):
#     def __init__(self, balance = 0):
#         self.balance = balance
#     def display_balance(self):
#         return f"Balance: ${self.balance}."
#     def deposit(self, amount):
#         self.balance += amount
#         return f"Deposited ${amount}. New balance: ${self.balance}."
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             return f"Withdrew ${amount}. New Balance: ${self.balance}."
#         else:
#             return "Insufficient funds."
# current_money = CurrentMoney(100)
# deposit = current_money.deposit(50)
# withdraw = current_money.withdraw(30)
# withdraw_2 = current_money.withdraw(1000)
# print("Current Money:", current_money.display_balance())
# print("Deposit:", deposit)
# print("Withdrawal:", withdraw)
# print("Withdrawal 2:", withdraw_2)