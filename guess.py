secret_word = "Dunnie"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count +=1
    else:
        out_of_guesses = True
        
if out_of_guesses:
    print("You are out of guesses, YOU LOSE")
else:
    print("You win!")
 #Running the while loop 
a = 1
while a < 10:
    print(a)
    a = a + 1
print("Done with loop")
 
 #Using the if statements to determine the maximum number
def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
       return num1
    elif num2 > num1 and num2 > num3:
       return num2
    else:
       return num3
     
print(max_num(200, 300, 400))

#Using the if statement to build a more advanced calculator
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
    print("INVALID OPERATOR")

#using the if statement and the Boolean
is_female = True
is_short = True

if is_female and is_short:
    print("You are a short Female")
elif is_female and not(is_short):
    print("You are a tall female")
else:
    print("You are neither a female nor short or both")
    
#Using loop
name = ["Dunnie", "Geestar", "Jay", "Eddy"]
for friends in name:
    print(friends)
    
#using the input
Name = input("Enter your name: ")
age = input("Enter your age: ")
school = input("Where do you study: ")
place = input("Where do you live: ")
city = input("Enter your city: ")
code = input("Enter your country code: ")
phone = input("Enter your phone number:254 ")
email = input("Enter your email: ")
address = input("Enter you address: ")

print("Hello " + Name + " You are! " + str(age) + " You study at " + school
    + " You live in " + place + " Your city is " + city + " Your country code is " + code
    + " Your phone number is " + phone + "Your email is " + email + " Your address is " + address)
















