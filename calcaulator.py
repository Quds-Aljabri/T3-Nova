import random

num1 = 0
num2 = 0
operator = " "


num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 1st number: "))

operator = input("Enter the operator  : ")

if  operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif  operator == "*":
    result = num1 * num2

elif  operator == "**":
    result = num2 * num1

elif  operator == "**":
    result = num1 ** num2

elif operator == "/":
    result = num1 / num2

elif  operator == "fac":
   answer = 1
   limit = num1
   while limit > 0:
       answer = answer * limit
       limit = limit - 1
       result = answer

elif operator == "abs":
    result = abs(num1), abs(num2)

elif operator == "random":
    result = random.randrange(num1, num2)



print(result)