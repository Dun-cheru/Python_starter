"""
Building a better calculator
Ability to perform more advanced mathematical calculations
"""
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))
#Figure the operator the user wanted to use so we use an if statement

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op ==  "*":
    print(num1 * num2)
else:
    print("Invalid operator")



#it does not add because it converts it as a string

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
add = num1 + num2

print(add)

#using in to for whole numbers
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)

print(result)

#using float for decimal number this are mostly used in caclulators
num3 = input("Enter a number: ")
num4 = input("Enter another number: ")
sum = float(num3) + float(num4)

print(sum)

