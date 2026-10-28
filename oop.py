# # example 1

# class Dog:
#     sound = "bark"
# # Creating object from class
# dog1 = Dog()
# print(dog1.sound)

# # example 2
# class Dog:
#     species = "Canine" # Class attribute
#     def __init__(self, name, age):
#         self.name = name # Instance attribute
#         self.age = age # Instance attribute
# # Creating an object of the Dog class
# dog1 = Dog("Buddy", 3)
# print(dog1.name)
# print(dog1.species)

## str()
# class Student:
#     def __init__(self, id, name, gender):
#         self.id = id
#         self.name = name
#         self.gender = gender

# s1 = Student(1001, "Dara", "Male")
# print(f"{s1.id}, {s1.name}, {s1.gender}")
# # <__main__.Student object at 0x0000025C56848830>
# class Student:
#     def __init__(self, name):
#         self.name = name

# stu = Student("Nita")
# print(stu)

# class Student:
#     def __init__(self, id, name, gender):
#         self.id = id
#         self.name = name
#         self.gender = gender
#     def __str__(self):
#         return (f"{self.id}, {self.name}, {self.gender}")
# s1 = Student(1001, "Dara", "Male")
# print(s1)
