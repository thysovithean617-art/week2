# 4
import math
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Enter an operator: ")
if op == "+":
    print("Result = ", num1 + num2)
elif op == "-":
    print("Result = ", num1 - num2)
elif op == "*":
    print("Result = ", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result = ", num1 / num2)
    else:
        print("Invalid!")
elif op == "%":
    print("Result = ", num1 % num2)
else:
    print("Invalid Operator!")