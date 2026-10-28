# def my_function(**myvar):
#     print("Type: ", type(myvar))
#     print("Name: ", myvar["name"])
#     print("Age: ", myvar["age"])
#     print("All data: ", myvar)

# my_function(name = "Dar", age = 30, city = "Phnom Penh")

# def my_function(username, **details):
#     print("Username:", username)
#     print("Additional details:")
#     for key, value in details.items():
#         print(" ", key + ":", value)

# my_function("dara123", age = 25, city = "Phnom Penh", hobby = "coding")

# def my_function(title, *args, **kwargs):
#     print("Title:", title)
#     print("Positional arguments:", args)
#     print("Keyword augrments:", kwargs)

# my_function("User info", "Emil", "Dara", age = 25, city = "Phnom Penh")

# def my_function(a, b, c):
#     return a + b + c

# numbers = [1, 2, 3]
# result = my_function(*numbers)
# print(result)

# def my_function(fname, lname):
#     print("Hello", fname, lname)

# person = {"fname" : "Dara", "lname" : "Sok"}
# my_function(**person)

# def message():
#     # local variables
#     mgs = "Hello Python"
#     print(f"I love you Python and {mgs}")
# message()

#Global variables
# st = "Hello Dara you learn Python right??"
# def student():
#     print(f"I love Python and {st}")
# student()
# print(f"This is me!! {st}")

# Global variables
# st = "Hello Dara you learn Python right??"
# def student():
#     # Local variable
#     st = "I love Python too"
#     print(f"I love Python and {st}")
# student()
# print(f"This is me!! {st}")

# Error
# def student():
#     # local variable
#     st += "I love Python too"
#     print(f"I love Python and {st}")

# st = "Hello Dara you learn Python right??"
# student()

# Correct
# s = "Python is great!"

# def fun():
#     global s
#     s += " Why you love Python"      # Modify global variable
#     print(s)
#     s = "Because it is easy to learn!"      # Reassign global
#     print(s)

# fun()
# print(s)

# Global vs Local with Same Name
# a = 1       # Global variable

# def f():
#     print("f():", a)        # Uses global a

# def g():
#     a = 2       # Local shadows global
#     print("g():", a)

# def h():
#     global a
#     a = 3       # Modifies global a
#     print("h():", a)

# print("global: ", a)
# f()
# print("global: ", a)
# g()
# print("global: ", a)
# h()
# print("global: ", a)

# Practice

# # 1
# def employee():
#     id = int(input("Enter an employee's ID: "))
#     name = str(input("Enter an employee's name: "))
#     sex = str(input("Enter an employee's sex: "))
#     salary = int(input("Enter an employee's salary: "))
#     rate = float(input("Enter an employee's rate: "))
#     hour = int(input("Enter an employee's hour: "))
#     total = salary + (rate * hour)
#     print("Total Salary: ", + total)

# employee()
# print()
# employee()

# # 2
# import math
# exchange_rate = 4100
# print("Enter 1 to exchange Riel to USD.")
# print("Enter 2 to exchange USD to Riel.")
# choice = int(input("Enter your choice(1/2): "))
# def riel():
#     riel = int(input("Enter Riel: "))
#     usd = riel / exchange_rate
#     print(usd)
# def usd():
#     usd = int(input("Enter USD: "))
#     riel = usd * exchange_rate
#     print(riel)
# if choice == 1:
#     riel()
# if choice == 2:
#     usd()

# # 3
# def myFun():
#     code = int(input("Enter a code: "))
#     name = str(input("Enter a name of a product: "))
#     qty = int(input("Quantity: "))
#     uprice = float(input("Enter a price of the item: "))
#     dis = int(input("Enter a discout: "))
#     overall = uprice * qty
#     totalDis = overall * (dis / 100)
#     total =float(overall - totalDis)
#     print(total)
# result = myFun()
# print(result)


# def decorator(func):
#     def wrapper():
#         print("Before calling the function.")
#         func()
#         print("After calling the function.")
#     return wrapper

# @decorator 
# def greet():
#     print("Hello, World!")
# greet()

# a = 'Python'
# upper = lambda x: x.upper()
# print(upper(a))

# check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
# print(check(5))
# print(check(-3))
# print(check(0))

# func = [lambda arg=x: arg * 10 for x in range(1, 5)]
# for i in func:
#     print(i())

# cal = lambda x, y: (x + y, x * y)
# res = cal(3, 4)
# print(res)

# c = [1, 2, 3, 4, 5, 6]
# even = filter(lambda x: x % 2 == 0, c)
# print(list(even))

# a = [1, 2, 3, 4]
# double = map(lambda x: x * 2, a)
# print(list(double))

# from functools import reduce
# a = [1, 2, 3, 4]
# mul = reduce(lambda x, y: x * y, a)
# print(mul)

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# # multiply
# mapped = list(map(lambda x: x * 2, numbers))
# print("Map: ", mapped)

# # select even numbers
# filtered = list(filter(lambda x: x % 2 == 0, numbers))
# print("Filter: ", filtered)

# # sum
# reduced = reduce(lambda x, y: x + y, numbers)
# print("Reduce: ", reduced)

# def greeting(name):
#     print("Hello : " + name)

# person = {
#     "name": "David",
#     "age": 18,
#     "city": "Phnom Penh",
#     "major": "Python"
# }

# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "major": "Python Developer"
# }