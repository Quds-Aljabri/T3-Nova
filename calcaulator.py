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

if  operator == "*":
    result = num1 * num2

print(result)