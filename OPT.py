# # # # import OT
# # # # OT.greeting("Hello World")

# # # # import OT
# # # # result = OT.person["age"]
# # # # print(result)

# # # # import OT as imf
# # # # result = imf.person["age"]
# # # # print(result)

# # # # import platform
# # # # x = platform.system()
# # # # print(x)

# # # # import platform
# # # # x = dir(platform)
# # # # print(x)

# # # # from OT import person
# # # # print(person["age"])

# # # # 1
# # # # import math
# # # # radius = int(input("Enter the lenght of radius: "))
# # # # def perimeter():
# # # #     p = 2 * math.pi * radius
# # # #     return p
# # # # def area():
# # # #     s = math.pi * radius * radius
# # # #     return s
# # # # per = perimeter()
# # # # are = area()
# # # # print("Perimeter of the circle: ", per)
# # # # print("Area of the circle: ", are)

# # # # 2
# # # # num = int(input("Enter a number from 1 to 100: "))
# # # # def randomNumber():
# # # #     if num >= 1 and num <= 100:
# # # #         print("Random number: ", num)
# # # #     else:
# # # #         print("Invalid number!")

# # # # randomNumber()

# # # # 3
# # # # import random
# # # # secretNum = random.randint(1, 10)
# # # # print("I'm thinking about a number, now guess it: ")
# # # # num = int(input("Enter your guess: "))
# # # # while num != secretNum:
# # # #     if(num < secretNum):
# # # #         print("Too low, try again!")
# # # #     elif(num > secretNum):
# # # #         print("Too high, try again!")
# # # #     num = int(input("Enter your guess: "))

# # # # print("Congratulation! You get the right number!")

# # # # import json
# # # # # some JSON:
# # # # x = '{"name":"John", "age":30, "city":"New York"}'
# # # # # parse x:
# # # # y = json.loads(x)
# # # # # the result is a Phython dictionary:
# # # # print(y["age"])

# # # # import json
# # # # # a Phython object (dict):
# # # # x = {
# # # #     "name":"John",
# # # #     "age": 30,
# # # #     "city":"New York"
# # # # }
# # # # # convert into JSON:
# # # # y = json.dumps(x)
# # # # # the result is a JSON string:
# # # # print(y)

# # # # import json
# # # # print(json.dumps({"name":"John", "age":30})) # dict
# # # # print(json.dumps(["apple", "bananas"])) # list
# # # # print(json.dumps(("apple", "bananas"))) # tuple
# # # # print(json.dumps("hello"))  # sting
# # # # print(json.dumps(42))   # int
# # # # print(json.dumps(31.76))    # float
# # # # print(json.dumps(True)) # True
# # # # print(json.dumps(False))    # False
# # # # print(json.dumps(None)) # None

# # # # import json

# # # # x = {
# # # #     "name": "John",
# # # #     "age": 30,
# # # #     "married": True,
# # # #     "divorced": False,
# # # #     "children": ("Ann", "Billy"),
# # # #     "pets": None,
# # # #     "Cars": [
# # # #         {"model": "BMW 230", "mpg": 27.5},
# # # #         {"model": "Fordd Edge", "mpg": 24.1}
# # # #     ]
# # # # }

# # # # print(json.dumps(x, indent = 4, separators=(". ", " = ")))

# # # # import json
# # # # x = {
# # # #     "name": "John",
# # # #     "sex": "Male",
# # # #     "age": 30
# # # # }
# # # # y = json.dumps(x)
# # # # print(y)


# # # # import json 
# # # # x= dict(
# # # #     id = int(input("Enter an ID: ")),
# # # #     name = str(input("Enter a name: ")),
# # # #     gender = str(input("Enter a gender (Male or Female): ")),
# # # #     age = int(input("Enter an age: ")),
# # # #     address = str(input("Enter an address: "))
# # # # )
# # # # y = json.dumps(x)
# # # # print(y)

# # # # import json
# # # # student = []
# # # # for i in range(5):
# # # #     print(f"\nstudent {i+1}")
# # # #     id = int(input("Enter student ID: "))
# # # #     name = str(input("Enter student name: "))
# # # #     gender = str(input("Enter student gender: "))
# # # #     score = int(input("Enter student score: "))
# # # #     student.append({
# # # #         "id": id,
# # # #         "name": name,
# # # #         "gender": gender,
# # # #         "score": score
# # # #     })

# # # # print("\n-----All Students-----")
# # # # for s in student:
# # # #     print(f"student {s}")

# # # # totalScore = [s["score"] for s in student]
# # # # print(sum(totalScore) / len(totalScore))
# # # # print(max(totalScore))
# # # # print(min(totalScore))
# # # # with open("student.json", "w") as file:
# # # #     json.dump(student, file, indent = 4)

# # # # my_file = open('emp.txt', 'w')
# # # # print("Hello World")
# # # # print(my_file)

# # # # f = open('emp.txt', 'r')
# # # # print("Filname: ", f.name)
# # # # print("Mode: ", f.mode)
# # # # print("Is Closed?", f.closed)

# # # # f.close()
# # # # print("Is Closed?", f.closed)

# # # # f = open("emp.txt", "r")
# # # # content = f.read()
# # # # print(content)

# # # # f.close()

# # # # with open("emp.txt", "a") as file:
# # # #     file.write("\nhello")
# # # # with open("student.txt", "a") as file:
# # # #     name = input("Enter a name: ")
# # # #     id = input("Enter an ID: ")
# # # #     gender = input("Enter the gender: ")
# # # #     score = input("Enter a score: ")
# # # #     file.write(f"\n{id} {name} {gender} {score}")
# # # # with open("student.txt", "a") as file:
# # # #     for i in range(5):
# # #         # id = input("Enter an ID: ")
# # #         # name = input("Enter a name: ")
# # #         # gender = input("Enter the gender: ")
# # #         # score = input("Enter a score: ")
# # #         # file.write(f"\n{id} {name} {gender} {score}")
# # # while True:
# # #     print("1. Add Student\n2. Show Student\n3. Exit")
# # #     choice = int(input("Enter your choice: "))
# # #     if choice == 1:
# # #         with open("student.txt", "w") as file:
# # #             id = input("Enter an ID: ")
# # #             name = input("Enter a name: ")
# # #             gender = input("Enter the gender: ")
# # #             score = input("Enter a score: ")
# # #             file.write(f"{id} {name} {gender} {score}\n")
# # #     elif choice == 2:
# # #         with open("student.txt", "r") as file:
# # #             content = file.read()
# # #             print(content)
# # #     elif choice == 3:
# # #         print("You exited!")
# # #         break
# # #     else:
# # #         print("Invalid choice!")

# # # import os
# # # os.remove("emp.txt")

# # # import csv
# # # with open("student.csv", "r", encoding="utf-8") as f:
# # #     reader = csv.reader(f)
# # #     print("-"*80)
# # #     print("ID\t\tName\t\tGender\t\tTotal\t\tAverage")
# # #     print("-"*80)
# # #     next(reader)
# # #     for row in reader:
# # #         math = int(row[5])
# # #         khmer = int(row[6])
# # #         english = int(row[7])
# # #         total = math + khmer + english
# # #         average = total / 3
# # #         print(row[0],"\t\t",row[1],"\t\t", row[2],"\t\t", total,"\t\t", average)

# # # for i in range(n):
# # #     id = int(input("ID: "))
# # #     name = str(input("Name: "))
# # #     gender = str(input("Gender: "))
# # #     age = int(input("Age: "))
# # #     math = int(input("Math score: "))
# # #     kh = int(input("Khmer score: "))
# # #     eng = int(input("English score: "))
# # #     bio = int(input("Biology score: "))
# # #     chem = int(input("Chemistry score: "))
# # #     his = int(input("History score: "))
# # #     phy = int(input("Physic score: "))
# # import csv
# # n = int(input("How many student? "))
# # choice = 0
# # while choice < 5:
# #     choice = int(input("Enter your choice: "))
# #     if choice == 1:
# #         with open("student.csv", "a", encoding="utf-8") as file:
# #             writer = csv.writer(file)

# #             for i in range(n):
# #                 id = int(input("ID: "))
# #                 name = str(input("Name: "))
# #                 gender = str(input("Gender: "))
# #                 age = int(input("Age: "))
# #                 math = int(input("Math score: "))
# #                 kh = int(input("Khmer score: "))
# #                 eng = int(input("English score: "))
# #                 bio = int(input("Biology score: "))
# #                 chem = int(input("Chemistry score: "))
# #                 his = int(input("History score: "))
# #                 phy = int(input("Physic score: "))

# #                 writer.writerow([
# #                     id,
# #                     name,
# #                     gender,
# #                     age,
# #                     math,
# #                     kh,
# #                     bio,
# #                     chem,
# #                     his,
# #                     phy
# #                 ])
# #     if choice == 2:
# #         print(f"Total student = {n}")
# #     if choice == 3:
# #         with open("student.csv", "r", encoding="utf-8") as f:
# #             reader = csv.reader(f)
# #             print("-"*80)
# #             print("ID\t\tName\t\tGender\t\tTotal")
# #             print("-"*80)
# #             next(reader)
# #             for row in reader:
# #                 math = int(row[4])
# #                 khmer = int(row[5])
# #                 english = int(row[6])
# #                 biology = int(row[7])
# #                 chemistry = int(row[8])
# #                 history = int(row[9])
# #                 physic = int(row[10])
# #                 total = math + khmer + english + biology + chemistry + history + physic
# #                 print(row[0],"\t\t",row[1],"\t\t", row[2],"\t\t", total)
# #     if choice == 4:
# #         with open("student.csv", "r", encoding="utf-8") as f:
# #             reader = csv.reader(f)
# #             print("-"*80)
# #             print("ID\t\tName\t\tGender\t\tAverage")
# #             print("-"*80)
# #             next(reader)
# #             for row in reader:
# #                 math = int(row[4])
# #                 khmer = int(row[5])
# #                 english = int(row[6])
# #                 biology = int(row[7])
# #                 chemistry = int(row[8])
# #                 history = int(row[9])
# #                 physic = int(row[10])
# #                 total = math + khmer + english + biology + chemistry + history + physic
# #                 avg = total / 3
# #                 print(row[0],"\t\t",row[1],"\t\t", row[2],"\t\t", avg)
#     # if choice == 5:
#     #     highestTotal = -1
#     #     stuScor = None
#     #     with open("student.csv", "r", encoding="utf-8") as f:
#     #         reader = csv.reader(f)
#     #         next(reader)
#     #         for row in reader:
#     #             total = int(row[4]) + int(row[5]) + int(row[6]) + int(row[7]) + int(row[8]) + int(row[9]) + int(row[10])
#     #             if total > highestTotal:
#     #                 highestTotal = total
#     #                 stuScor = row

#     #         print(highestTotal)
# #     if choice == 6:
# #         lowestTotal = 700
# #         student = None
# #         with open("student.csv", "r", encoding="utf-8") as f:
# #             reader = csv.reader(f)
# #             next(reader)
# #             for row in reader:
# #                 total = int(row[4]) + int(row[5]) + int(row[6]) + int(row[7]) + int(row[8]) + int(row[9]) + int(row[10])
# #                 if total < lowestTotal:
# #                     lowestTotal = total
# #                     student = row
# #             print(lowestTotal)
# #     if choice == 7:
# #         search_name = input("Search Name: ")
# #         with open("student.csv", "r", encoding="utf-8") as f:
# #             reader = csv.reader(f)
# #             found = False
# #             for row in reader:
#             #     if row[1] == search_name:
#             #         print(row)
#             #         found = True
#             #         break
#             # if not found:
#             #     print("Student Not Found")
# #     if choice == 8:
# #         with open("student.csv", "r", encoding="utf-8") as f:
# #             reader = csv.reader(f)
# #             countFemale = 0
# #             countMale = 0
# #             for row in reader:
# #                 if row[2] == "Female":
# #                     countFemale += 1
# #                 else:
# #                     countMale += 1
# #             print(f"There are {countFemale} females and {countMale} males!")
# #     if choice == 9:
# #         with open("student.csv", "r", encoding="utf-8") as f:
# #             reader = csv.reader(f)
# #             next(reader)
# #             for row in reader:
# #                 total = int(row[4]) + int(row[5]) + int(row[6]) + int(row[7]) + int(row[8]) + int(row[9]) + int(row[10])
# #                 average = total / 7
# #                 if average >= 90:
# #                     print("Student get grade A.")
# #                 elif average >= 80:
# #                     print("Student get grade B.")
# #                 elif average >= 70:
# #                     print("Student get grade C.")
# #                 elif average >= 60:
# #                     print("Student get grade D.")
# #                 elif average >= 50:
# #                     print("Student get grade E.")
# #                 else:
# #                     print("Student repeat year!")
# #     if choice >= 10:
# #         print("You exited!")
# #         break

# # # import csv
# # # name = input("Search Name: ")
# # # with open("student.csv", "r") as file:
# # #     reader = csv.reader(file)
# # #     found = False
# # #     for row in reader:
# # #         if row[1] == name:
# # #             print(row)
# # #             found = True
# # #             break
# # #     if not found:
# # #         print("Student Not Found")

# import csv 
# def show_all_employees():
#     with open("emp.csv", "r") as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             print(f"ID: {row[0]}\nName: {row[1]}\nGender: {row[2]}\nAge: {row[3]}\nPosition: {row[4]}\nBasic Salary: {row[5]}\nRate: {row[6]}\nHour: {row[7]}")

# def count_employees():
#     empCount = 0
#     with open("emp.csv", "r") as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             empCount += 1
#         print(f"Total Employees = {empCount}")

# def calculate_salary():
#     with open("emp.csv", "r") as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             overtime = int(row[6]) * int(row[7])
#             total_salary = int(row[5]) + overtime
#             print(f"ID: {row[0]}\nName: {row[1]}\nRate: {row[6]}\nHour: {row[7]}\nOvertime: {overtime}\nTotal Salary: {total_salary}")

# def average_salary():
#     with open("emp.csv", "r") as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             overtime = int(row[6]) * int(row[7])
#             total_salary = int(row[5]) + overtime
#             avg = total_salary / 5
#         print(f"Average Salary: {avg}")

# def highest_salary():
#     highestTotal = -1
#     employee = None
#     with open("emp.csv", "r") as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             overtime = int(row[6]) * int(row[7])
#             total_salary = int(row[5]) + overtime
#             if highestTotal < total_salary:
#                 highestTotal = total_salary
#                 empoyee = row
#     print(f"Name: {row[1]}\nPosition: {row[4]}\nTotal Salary: {highestTotal}")

# def lowest_salary():
#     lowestTotal = 1000
#     emp = None
#     with open("emp.csv", "r") as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             overtime = int(row[6]) * int(row[7])
#             total_salary = int(row[5]) + overtime
#             if lowestTotal > total_salary:
#                 lowestTotal = total_salary
#                 emp = row
#         print(f"Name: {row[1]}\nPosition: {row[4]}\nTotal Salary: {lowestTotal}")

# def search_employee():
#     name = input("Search Name: ")
#     with open("emp.csv", "r") as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             overtime = int(row[6]) * int(row[7])
#             total_salary = int(row[5]) + overtime
#             if row[1] == name:
#                 print(f"ID: {row[0]}\nName: {row[1]}\nGender: {row[2]}\nAge: {row[3]}\nPosition: {row[4]}\nBasic Salary: {row[5]}\nRate: {row[6]}\nHour: {row[7]}\nOvertime: {overtime}\nTotal Salary: {total_salary}")
#                 found = True
#                 break
#             if not found:
#                 print("Employee Not Found")

# def count_male_or_female():
#     count_male = 0
#     count_female = 0
#     with open("emp.csv", "r") as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             if row[2] == "F":
#                 count_female += 1
#             else:
#                 count_male += 1
#     print(f"Male = {count_male}\nFemale = {count_female}")

# def salary_report():
#     with open("emp.csv", "r") as file:
#         reader = csv.reader(file)
#         print("="*120)
#         print("ID \t\t Name \t\t Position \t\t Basic \t\t\t OT \t\t Total Salary")
#         print("="*120)
#         next(reader)
#         for row in reader:
#             overtime = int(row[6]) * int(row[7])
#             total_salary = int(row[5]) + overtime
#             print(f"ID: {row[0]} \t Name: {row[1]} \t Position: {row[4]} \t Basic Salary: {row[5]} \t Overtime: {overtime} \t Total Salary: {total_salary}")

# Menu = "========== EMPLOYEE MANAGEMENT SYSTEM ==========\n1. Show All Employees\n2. Count Employees\n3. Calculate Salary\n4. Average Salary\n5. Highest Salary\n6. Lowest Salary\n7. Search Salary\n8. Count Male/Female\n9. Salary Report\n10. Exit"
# while True:
#     print(Menu)
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         show_all_employees()
#     elif choice == 2:
#         count_employees()
#     elif choice == 3:
#         calculate_salary()
#     elif choice == 4:
#         average_salary()
#     elif choice == 5:
#         highest_salary()
#     elif choice == 6:
#         lowest_salary()
#     elif choice == 7:
#         search_employee()
#     elif choice == 8:
#         count_male_or_female()
#     elif choice == 9:
#         salary_report()
#     else: 
#         print("You have exited!")
#         break

# import json

# student = {
#     "id": 1,
#     "name": "Dara",
#     "gender": "Male",
#     "score": 90
# }

# with open("student.json", "w") as file:
#     json.dump(student, file)

# import json

# with open("student.json", "r") as file:
#     data = json.load(file)

# print(data)

# import json

# student = {
#     "name": "Dara",
#     "score": 90
# }

# text = json.dumps(student)
# print(text)

# import json
# text = '{"name": "Dara", "score": 90}'
# student = json.loads(text)
# print(student)

# import json
# students = [
#     {"id": 1, "name": "Sok", "score": 90},
#     {"id": 2, "name": "Dara", "score": 80},
#     {"id": 3, "name": "Nita", "score": 95}
# ]

# with open("student.json", "w") as file:
#     json.dump(students, file, indent = 4)

# import json
# with open("student.json", "r") as file:
#     students = json.load(file)

# for i in students:
#     print(i)

import json
with open("student.json", "r") as file:
    students = json.load(file)

students.append({
    "id": 4,
    "name": "Vanna",
    "score": 88
})

# with open("student.json", "w") as file:
#     json.dump(students, file, indent = 4)

# import json
# name = input("Search name: ")
# with open("student.json", "r") as file:
#     students = json.load(file)

# found = False

# for student in students:
#     if student["name"] == name:
#         print(student)
#         found = True
#         break

# if not found:
#     print("Student Not Found")

# import json
# id = int(input("Input ID: "))
# with open("student.json", "r") as file:
#     students = json.load(file)

# for student in students:
#     if student["id"] == id:
#         student["score"] = 100

# with open("student.json", "w") as file:
#     json.dump(students, file, indent = 4)

# import json
# id = int(input("Input ID: "))
# with open("student.json", "r") as file:
#     students = json.load(file)

# students = [student for student in students if student["id"]  != id]

# with open("student.json", "w") as file:
#     json.dump(students,file, indent = 4)


# Create a system that can store employees' information
import json
emp = [
    {"id": 1, "name": "Dara", "gender": "Male", "position": "Manager", "salary": 1500},
    {"id": 2, "name": "Nita", "gender": "Female", "position": "Accounting", "salary": 500},
    {"id": 3, "name": "Vanna", "gender": "Male", "position": "CEO", "salary": 100}
]
with open("employee.json", "w") as file:
    json.dump(emp, file, indent = 3)

# Create a Menu
# Add employees
def add():
    with open("employee.json", "r") as file:
        emp = json.load(file)

    id = int(input("Enter ID: "))
    name = input("Enter name: ")
    gen = input("Enter gender: ")
    pos = input("Enter position: ")
    sal = int(input("Enter salary: "))
                 
    # newEmp = {
    #     "id" = id,
    #     "name" = name,
    #     "gender" = gender,
    #     "position" = position,
    #     "salary" = salary
    # }
    emp.append({
        "id" = id,
        "name" = name,
        "gender" = gen,
        "position" = pos,
        "salary" = sal
    })
    with open("employee.json", "w") as file:
        json.dump(emp, file, indent = 4)

# Show employees' information
def show():
    with open("employee.json", "r") as file:
        reader = json.reader(file)
        next(reader)
        for i in emp:
            print(f"ID: {id}\nName: {name}\nGender: {gender}\nPosition: {position}\nSalary: {salary}")

# Search for an employee
def search():
    id = int(input("Search ID: "))
    with open("employee.json", "r") as file:
        emp = json.load(file)
    found = False
    for i in emp:
        if i["id"] == id:
            print(emp)
            found = True
            break
    if not found:
        print("Employee Not Found")

# Update 
def update():
    id = int(input("Search ID: "))
    with open("employee.json", "r") as file:
        emp = json.load(file)
    for i in emp:
        if i["id"] == id:
        
