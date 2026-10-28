# # name = "Thean"
# # age = 21
# # high = 1.23

# # print(name)
# # print(age)
# # print(high)

# # print(type(name))
# # print(type(age))
# # print(type(high))


# # # List
# # a = [1, 2, 3]
# # print(a)
# # # access with index
# # b = ["apple", "For", "apples", 4, 5]
# # print(b[3])
# # print(b[-3])

# # # Tuple
# # t1 = (1,)
# # print(type(t1))

# # t2 = ('applees', 'For', 'apples', 1, 2)
# # print(t2[3])
# # print(t2[-3])

# # # Boolean Data Type
# # print(type(True))
# # print(type(False))
# # if 1:
# #     print("1 is truthy")
# # if not 0:
# #     print("0 is falsy")


# # # Set data type
# # s1 = {"a", "a", "b", "c", "b"}
# # print(s1)

# # s2 = {"apples", "For", "apples", "banana", "banana"}
# # for i in s2:
# #     print(i)


# # # Dictionary data type
# # d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# # print(d[1])
# # print(d.get(2))

# # # Acessing Items
# # thisdict = {
# #     "brand": "Ford",
# #     "model": "Mustang",
# #     "year": 1964
# # }
# # x = thisdict["brand"]
# # print(x)
# # y = thisdict.get("model")
# # print(y)

# # # change value
# # thisdict["year"] = 2018
# # print(thisdict)

# # # update dictionary 1
# # thisdict.update({"year": 2026})
# # print(thisdict)

# # # Add dictionary items
# # thisdict["color"] = "black"
# # print(thisdict)

# # # update dictionary 2
# # thisdict.update({"color": "lavender"})
# # print(thisdict)

# # Remove dictionary items 1: using pop()
# # students = {
# #     "id": 101,
# #     "name": "Dara",
# #     "sex": "Male",
# #     "address": "Takeo"
# # }
# # print(students)
# # students.pop("sex")
# # print(students)

# # Remove dictionary items 2: using popitem(), remove the last item
# # students = {
# #     "id": 101,
# #     "name": "Dara",
# #     "sex": "Male",
# #     "address": "Takeo"
# # }
# # print(students)
# # students.popitem()
# # print(students)

# # Remove dictionary items 3: using del, delete the dictionary completely
# # students = {
# #     "id": 101,
# #     "name": "Dara",
# #     "sex": "Male",
# #     "address": "Takeo"
# # }
# # print(students)
# # del students
# # print(students)

# # Remove dictionary items 4: using clear(), make it empty
# # students = {
# #     "id": 101,
# #     "name": "Dara",
# #     "sex": "Male",
# #     "address": "Takeo"
# # }
# # print(students)
# # students.clear()
# # print(students)


# # # Copy dictionary
# # Assign value
# # student1 = {
# #     "name": "Nika",
# #     "age": 20
# # }
# # print(student1)
# # student2 = student1
# # student2["age"] = 25
# # print(student1)
# # print(student2)

# # Using .copy() method
# # student1 = {
# #     "name": "Nika",
# #     "age": 20
# # }
# # student2 = student1.copy()
# # student2["age"] = 25
# # print(student1)
# # print(student2)

# # Proof .copy() method
# # car1 = {
# #     "brand": "Toyota",
# #     "color": "Red"
# # }
# # car2 = car1.copy()
# # car2["color"] = "Blue"
# # print("car1 = ", car1)
# # print("car2 = ", car2)


# # # Nested Dictionary
# # Method 1
# # myfamily = {
# #     "child1": {
# #         "name": "Dara",
# #         "year": 2004
# #     },
# #     "child2": {
# #         "name": "Nita",
# #         "year": 2007
# #     },
# #     "child3": {
# #         "name": "Davit",
# #         "year": 2011
# #     }
# # }
# # print(myfamily)

# # Method 2
# # child1 = {
# #     "name": "Dara",
# #     "year": 2004
# # }
# # child2 = {
# #     "name": "Nita",
# #     "year": 2007
# # }
# # child3 = {
# #     "name": "Davit",
# #     "year": 2011
# # }

# # myfamily = {
# #     "child1": child1,
# #     "child2": child2,
# #     "child3": child3
# # }

# # print(myfamily)

# # Access items in Nested Dictionary
# # myfamily = {
# #     "child1" : {
# #         "name" : "Dara",
# #         "year" : 2004
# #     },
# #     "child2" : {
# #         "name" : "Nita",
# #         "year" : 2007
# #     },
# #     "child3" : {
# #         "name" : "Davith",
# #         "year" : 2011
# #     }
# # }

# # print(myfamily["child2"]["name"])

# # Loop through Nested Dictionary: using .items()
# # myfamily = {
# #     "child1" : {
# #         "name" : "Dara",
# #         "year" : 2004
# #     },
# #     "child2" : {
# #         "name" : "Nita",
# #         "year" : 2007
# #     },
# #     "child3" : {
# #         "name" : "Davith",
# #         "year" : 2011
# #     }
# # }
# # for x, obj in myfamily.items():
# #     print (x)

# #     for y in obj:
# #         print(y + ':', obj[y])


# # # Challenge Example: About Dictionaries
# # book = {
# #     "title" : "Python",
# #     "author" : "Guido van Rosssum",
# #     "year" : 1991
# # }
# # print(book["author"])
# # book.update({"sex" : "Male"})
# # book.pop("title")
# # print(book)


# # # Condition Statement in Python
# # Example 1
# # i = 10
# # if i > 15:
# #     print("10 is less than 15")

# # print("In valid")

# # Example 2
# # a = 33
# # b = 200
# # if b > a:
# #     print("b is greater than a")

# # age = 19
# # if age > 18: print("Eligible to vote.")

# # age = 10
# # if age <= 12:
# #     print("Travel for free.")
# # else:
# #     print("Pay for ticket.")

# # number = 5
# # if number % 2 == 0:
# #     print("Even number")
# # else:
# #     print("Odd number")

# # score = 85
# # if score >= 90:
# #     print("Grade A")
# # elif score >= 80:
# #     print("Grade B")
# # elif score >= 70:
# #     print("Grade C")
# # else:
# #     print("Fail!")

# # age = 25
# # if age <= 12:
# #     print("Child")
# # elif age <= 19:
# #     print("Teenager")
# # elif age <= 35:
# #     print("Young adult")
# # else:
# #     print("Adult.")

# # i = 10
# # if i == 10:
# #     if i < 15:
# #         print("i is smaller than 15")

# #     if i < 12:
# #         print("i is smaller than 12 too")
# #     else:
# #         print("i is greater than 15")
# # else:
# #     print("i is not equal to 10")

# # score = 85
# # attendace = 90
# # submitted = True

# # if score >= 60:
# #     if attendace >= 80:
# #         if submitted:
# #             print("Pass with good standing")
# #         else:
# #             print("Pass but missing assignment")
# #     else:
# #         print("Passs but low attendace")
# # else:
# #     print("Fail")


# # # Challenge: IF...Else Basics
# # age = 20
# # if age <= 13:
# #     print("Child")
# # elif age < 18:
# #     print("Teenager")
# # else:
# #     print("Adult")


# # # Login System Using If Else in Python
# # username = "admin"
# # password = 1234
# # username = str(input("Enter your username: "))
# # password = int(input("Enter your passsword: "))
# # if username == "admin" and password == 1234:
# #     print("Login Success")
# # else:
# #     print("Wrong username or password")


# # # The Python Match Statement
# # day = 3

# # match day:
# #     case 1:
# #         print("Monday")
# #     case 2:
# #         print("Tuesday")
# #     case 3:
# #         print("Wednesday")
# #     case 4:
# #         print("Thursday")
# #     case 5:
# #         print("Friday")
# #     case 6:
# #         print("Saturday")
# #     case 7:
# #         print("Sunday")
# #     case _:
# #         print("Invalid day")

# # Calculator
# # num1 = int(input("Enter the first number: "))
# # num2 = int(input("Enter the second number: "))
# # op = input("Enter an operator (+, -, *, /): ")

# # match op:
# #     case "+" : print("Result = ", num1 + num2)
# #     case "-" : print("Result = ", num1 - num2)
# #     case "*" : print("Result = ", num1 * num2)
# #     case "/" : print("Result = ", num1 / num2)
# #     case _ : print("Invalid operator!")

# # Challenge The End Conditional Statement In Python
# # num1 = int(input("Enter the first number: "))
# # num2 = int(input("Enter the second number: "))
# # op = input("Enter an operator: ")

# if op == "+":
#     print("Result = ", num1 + num2)
# elif op == "-":
#     print("Result = ", num1 - num2)
# elif op == "*":
#     print("Result = ", num1 * num2)
# elif op == "/":
#     if num2 != 0:
#         print("Result = ", num1 / num2)
#     else:
#         print("Invalid!")
# elif op == "%":
#     print("Result = ", num1 % num2)
# else:
#     print("Invalid Operator!")
# # import math
# # a = int(input("Enter the number of a: "))
# # b = int(input("Enter the number of b: "))
# # c = int(input("Enter the number of c: "))
# # print("Formula: ax^(2) + bx^(1)+ c = 0\n")
# # if a == 0:
# #     print("Invalid value!")
# # else:
# #     delta = b**2 - 4*a*c
# #     if delta  > 0:
# #         x1 = (-b + math.sqrt(delta) / 2*a)
# #         x2 = (-b - math.sqrt(delta) / 2*a)
# #         print(x1)
# #         print(x2)
# #     elif delta == 0:
# #         x =-b/2*a
# #         print(x)
# #     else:
# #         print("This equation has no answer!")

# # Example 1
# # num = 0
# # while (num < 3):
# #     num = num + 1
# #     print("I love Python!")

# # Example 2
# # i = 0
# # while i < 10:
# #     print(i)
# #     i += 1

# # Use break
# # i = 1
# # while i < 10:
# #     print(i)
# #     if(i == 6):
# #         break
# #     i += 1

# # Use continue
# # i = 0
# # while i < 10:
# #     i += 1
# #     if i == 4:
# #         continue
# #     print(i)

# # Use else
# # i = 1
# # while i < 5:
# #     print(i)
# #     i += 1
# # else:
# #     print("i is no longer less than 5")

# # Use for loop
# # n = 4
# # for i in range (0, n):
# #     print(i)

# # fruits = ["apple", "banana", "cherry"]
# # for x in fruits:
# #     print(x)

# # Use with break
# # fruits = ["apple", "banana", "cherry"]
# # for x in fruits:
# #     print(x)
# #     if x == "banana":
# #         break

# # Use with continue
# # fruits = ["apple", "banana", "cherry"]
# # for x in fruits:
# #     if x == "banana":
# #         continue
# #     print(x)

# ## The range() Function

# # for x in range(6):
# #     print(x)
# #range(2, 6)
# # for x in range(2, 6):
# #     print(x)
# #range(2, 30, 3)
# # for x in range(2, 30, 3):
# #     print(x)

# # # Nested loop in Python

# # for i in range(1, 6):
# #     for  j in range(i):
# #         print(i, end = ' ')
# #     print()

# # adj = ["red", "big", "tasty"]
# # fruits = ["apple", "banana", "cherry"]

# # for x in adj:
# #     for y in fruits:
# #         print(x, y)

# # Ex1
# # x = [1, 2]
# # y = [4, 5]

# # for i in x:
# #     for j in y:
# #         print(i, j)

# # Ex2
# # for i in range(2, 4):
# #     for j in range(1, 11):
# #         print(i, "*", j, "=", i*j)
# #     print()

# # Ex3
# # Printing using different inner and outer nested loops
# # list1 = ['I am', 'Love Python']
# # list2 = ['Learn', 'every', 'days']

# # list2_size = len(list2)
# # for item in list1:

# #     print("Start outer for loop")
# #     i = 0
# #     while(i < list2_size):
# #         print(item, list2[i])
# #         i = i + 1
# #     print("End for loop")
# #     print()

# # Using break statement in nested loops
# # for i in range(2, 5):
# #     for j in range(1, 11):
# #         if i == j:
# #             break
# #         print(i ,"*", j, "=", i*j)
# #     print()

# # # Using continue statement in nested loops
# # for i in range(2, 5):
# #     for j in range(1, 11):
# #         if i == j:
# #             continue
# #         print(i ,"*", j, "=", i*j)
# #     print()

# # # Single-Line Nested Loops Using list Comprehension

# # l1 = []

# # for  i in range(5):
# #     row = []

# #     for j in range(3):
# #         row.append(j)

# #     l1.append(row)

# # print(l1)

# # l1 = [[j for i in range(3)]
# #          for i in range(5)]
# # print(l1)

# # # Functiona in Python
# # def my_function():
# #     print("Hello from a function of Python")

# # my_function()
# # my_function()
# # my_function()

# # def get_greeting():
# #     return "Hello from a function of Python"

# # # message = get_greeting()
# # # print(message)
# # print(get_greeting())

# ## Python Function Arguments
# # def my_function(fname):
# #     print(fname + " Hello")

# # my_function("Dara")
# # my_function("David")
# # my_function("Karuna")

# ## Parameters vs Arguments

# # def my_function(name):
# #     print("Hello", name)

# # my_function("Sokha")

# ## Default Parameter Values

# # def my_function(country = "Norway"):
# #     print("I am from", country)

# # my_function("Sweden")
# # my_function("India")
# # my_function()
# # my_function("Brazil")

# ## Passing Different Data Types

# # def my_function(fruits):
# #     for fruit in fruits:
# #         print(fruit)

# # my_fruits = ["apple", "banana", "cherry"]
# # my_function(my_fruits)

# ## Sending a dictionary as an argument

# # def my_function():
# #     return ["apple", "banana", "cherry"]

# # fruits = my_function()
# # print(fruits[0])
# # print(fruits[1])
# # print(fruits[2])

# # def my_student(name,message):
# #     print(f"This is: {name} {message}")
# # my_student(message="hello daro", name="Dara")

# # def my_employee(a,b):
# #     return a + b
# # results = my_employee(12,25)
# # print(results)
    

# # def my_function():
# #     return (10, 20)

# # x, y = my_function()
# # print("x: ", x)
# # print("y: ", y)

# ## Homeword
# import math
# print("CALCULATER")
# i = 1
# while i == 1:
#     print()
#     num1 = int(input("Enter the first number: "))
#     op = input("Enter an operater: ")
#     num2 = int(input("Enter the second number: "))
#     if op == "+":
#         print("Result = ", num1 + num2)
#     elif op == "-":
#         print("Result = ", num1 - num2)
#     elif op == "*":
#         print("Result = ", num1 * num2)
#     elif op == "/":
#         if num2 != 0:
#             print("Result = ", num1 / num2)
#         else:
#             print("Invalid!")
#     elif op == "%":
#         print("Result = ", num1 % num2)
#     else:
#         print("Invalid Operator!")
#     i = 0
#     print()
#     print("Enter 1 to continue calculating, otherwise stop.")
#     i = int(input("Enter your option: "))
#     if i != 1:
#         print("You have stopped calculating!")
#         break

# def my_function(*students):
#     print("The youngest child is " + students[2])

# my_function("Lita", "Sokha", "Dara")

# def my_function(*args):
#     print("Type: ", type(args))
#     print("First agrument: ", args[0])
#     print("Second argument: ", args[1])
#     print("All arguments: ", args)

# my_function("Lita", "Dara", "Sokha")

# def my_function(greeting, *names):
#     for name in names:
#         print(greeting, name)

# my_function("Hello", "Dara", "Nita", "Sokha")

# def my_function(**myvar):
#     print("Type: ", type(myvar))
#     print("Name: ", myvar["name"])
#     print("Age: ", myvar["age"])
#     print("All data: ", myvar)

#     my_function(name = "Dar", age = 30, city = "Phnom Penh")