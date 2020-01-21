is_male = True

if is_male:
    print("you are a male")
else:
    print("You are not a male")
#...........................................................................
is_male = True
is_tall = True
#using the OR operator
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither a male or tall")
#...........................................................................
is_male = True
is_tall = True
#using the AND operator
if is_male and is_tall:
    print("You are a tall male")
else:
   print("You are either a male but not tall")
#............................................................................
is_male = False
is_tall = False
#using the else if
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
else:
    print("you are either not a male or tall or both")

#using IF statements and comparison

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
       return num1
    elif num2 >= num1 and num2 >= num3:
       return num2
    else:
       return num3
print(max_num(100, 900, 700))
#Building a more advanced calculator
num1 = float(input("Enter the first number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter the second number: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
