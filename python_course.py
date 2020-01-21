print("   /|")
print("  / |")
print(" /  |")
print("/___|")

"""
 WITHOUT ANY VARIABLE
"""
print("There once was a man named Dunnie, ")
print("he was 22 years old. ")
print("He really liked the name Dee, ")
print("but he didn't like being 22.")

"""
WITH A VARIABLE INCLUDED AND A STRING
"""

##character_name is called a varible.
##"Gee" whatever is inside the double quotes is called a string.
character_name = "Gee"
character_age = "18"
is_Female = True
print("There was once a lady named " + character_name +  ", ")
print("she was " + character_age + "years old. ")
print("She really liked the name " + character_name + ", ")
print("but she didn't like being " + character_age + ".")

"""
using the STRING

"""
#\n is used to break the line to move to the next
print("Dee\nXperts")

#creating a STRING variable
phrase = "Dee Xperts"
print(phrase)

#concatenation joining multiple strings.
phrase = "Dee Xperts"
print(phrase + " is a cool place to study computer")

"""
Using the FUNCTION to operate a specific function in a line of code
"""
#you can use either lower or upper
phrase = "Dee Xperts is an institution that offers the best programming course"
print(phrase.lower())
phrase = "My name is DunnieBoY i'm the best programmer"
print(phrase.upper())

#we can use 'is' to determine whether it is upper case or lower case
phrase = "dunnie is a computer wizard"
print(phrase.upper().isupper())

#we use (len) to determine the length of the characters
Name = "DunnieBoY Gee and Dee"
print(len(Name))

#we use [] to specify a letter in a string
Name = "Dunnie"
print(Name[0])

#we use the function index to determine the number of the letter specified
Name = "GeeStar"
print(Name.index("S"))

#we can also use the function replace
Name  = "GeeStar"
print(Name.replace("GeeStar", "Dunnieboy"))

"""
Working with NUMBERS 
"""
#working with integers
a = 20
b = 30
sum = a + b
print(sum)

#use of parathesis for order of execution
print(2* (4 + 5))
print(2 * 4 + 5 )

# use of % to divide a number and also output a reminder
print(100 % 3)

#storing a number in a variable
my_num = 20
print(my_num)

#Adding a number and a string( if you don't add the string python will not execute the output)
my_num = 8
print(str(my_num) + " is my favourite number")

#using absolute to show the actual value
my_num = -29
print(abs(my_num))

#use pow to raise the a number by its power
print(pow(3, 3))

#use of max and min will output the greater and a lesser number between the two
print(max(29, 30))
print(min( 29, 30))

#using round to round off a number
print(round(2.7))

#using import to import some other math function from external sources
from math import *

#use of floow will take out the smallest number in a line of code
print(floor(2.7))

#use of ceil to roundup the number only
print(ceil(3.2))
#use pf sqrt to get the squareroot of a number
print(sqrt(64))

"""
Working with lists in python
"""
#use a descriptive name use the square brackets to add a bunch of values
friends = ["Dunnie", "Geestar", "Wiiliam", "Eddy"]
#Accessing individual elements in a list
print(friends)
#use index to access a value in a list
print(friends[0])
#selecting multiple value in a list
print(friends[1:])
#selecting a value within a certain range
print(friends[0:3])
#changing a value in a list
friends[1] = "Prosper"
print(friends[1:])
"""
working with list FUNCTIONS
"""
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Dunnie", "Eddy", "Hermon", "Geestar", "Dee"]

print(friends, lucky_numbers)
#use the extend function to add the second list
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Dunnie", "Eddy", "Hermon", "Geestar", "Dee"]
friends.extend(lucky_numbers)
print(friends)

#use the append function to add an individual list
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Dunnie", "Eddy", "Hermon", "Geestar", "Dee"]
friends.append("Creed")
print(friends)

#use insert function to add value in the middle of a list
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Dunnie", "Eddy", "Hermon", "Geestar", "Dee"]
friends.insert(1, "Emily")
print(friends)
#use remove function to delete a value from a list
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Dunnie", "Eddy", "Hermon", "Geestar", "Dee"]
friends.remove("Dee")
print(friends)
#use clear function to delete every value in a list
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Dunnie", "Eddy", "Hermon", "Geestar", "Dee"]
friends.clear()
print(friends)
#use of pop function to remove the last value in a list
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Dunnie", "Eddy", "Hermon", "Geestar", "Dee"]
friends.pop()
print(friends)
#use of index to determine whether a value exists in a list
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Dunnie", "Eddy", "Hermon", "Geestar", "Dee"]
print(friends.index("Hermon"))
#use of count function to know the number of items sharing the same value in a list
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Dunnie", "Eddy", "Hermon", "Geestar", "Dee", "Geestar"]
print(friends.count("Geestar"))
#use of sort function to arrange the values in a list
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Dunnie", "Eddy", "Hermon", "Geestar", "Dee", "Geestar"]
friends.sort()
print(friends)
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Dunnie", "Eddy", "Hermon", "Geestar", "Dee", "Geestar"]
lucky_numbers.sort()
print(lucky_numbers)
#use of reverse function
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Dunnie", "Eddy", "Hermon", "Geestar", "Dee", "Geestar"]
lucky_numbers.reverse
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

#CALCULATOR
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

#INPUT
"""
Getting input from users
"""
name = input("Enter your name: ")
age = input("Enter your age: ")
phone = input("Enter your phone number: 254")
country = input("Country: ")
email = input("Enter your email: ")
work = input("Where did you work: ")
study = input("Where do you study: ")
print("Hello " + name  + "! You are " + age  + " Your phone number is "
    + phone + " You live in " + country + " Your Email is " + email +
      " You work in " + work + " you studied at! " + study)


#THE IF STATEMENT
"""
we use IF statements to make decisions when they true or false
"""
#creating a boolean variable
# IF ==> is a condition
# Else ==> is an othewise

is_male = False
is_tall = True

if is_male:
    print("You are a male")
else:
    print("You are not a male")
if is_tall:
    print("You are tall")
else:
    print("You are not tall")

#you can as well combine both statements using or
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male or tall")
#using the AND operator
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are neither a male or tall")
#Adding Else If when he is short for our instance here
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a  tall male")
elif is_male and not(is_tall):
    print("You are a short male")
else:
    print("You are not a male or not tall")

"""
IF STATEMENTS AND COMPARISONS
"""
def max_num(num1, num2, num3):
    #(!=)not equal
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 40, 5))

#THE GUESS GAME
"""we create a while loop to prompt the user
to keep n guessing the word every time till they get it correctly"""
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("out of Guesses, YOU LOsE!")
else:
    print("You win!")

#THE MADLIBS GAME
color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a Celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
#create more madlibs

#WHILE LOOP
"""
while loop allows us to execute a code multiple times repeatedly while false
"""
#creating a variable
#we create a while loop using a condition
i = 1
while i <= 10:
    print(i)
    i = i + 1

print("Done with loop")

#THE RETURN STATEMENT

def cube(num):
    return num*num*num

result = cube(4)
print(result)

def square(num):
    return num*num
result = square(6)
print(result)
# NB after the return statement you cannot add another code  because it breaks the function

#THE LOOP 
"""
looping every letter in the loop
"""
for letter in "Dee Xperts":
    print(letter)

#create an array
friends = ["Dee", "Gee", "Dunnie", "Geestar"]
for name in (friends):
    print(name)

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not First")

#looping number between 0 to 10 but will not print 10
for index in range(10):
    print(index)

#specifying the range
for index in range (3, 10):
    print(index)

#THE TUPLES
"""
Container where you can store different values
"""
coordinates = (4, 5)
#Tuples cannot be modified
print(coordinates[0])
#differemce between a tuple and a list is that a list can be modified
#For a list we use square brackets but for a tuple we use paranthesis

coordinate = [44, 5]
coordinate[1] = (7)
print(coordinate[1])

#THE FUNCTIONS
"""
Function is a collection of code which performs a specific task
"""
#d ef is used to describe that this is a code
# Now we call the function in order to do that we type the functions name
def say_hi(name, age, study, work, occupation):
    print("Hello " + name + " You are ! " + str(age) + ", years old "
          + " You studied at" + study + ", you work at " + work + " Currently " + occupation)
say_hi("Dee", 22, "The Technical University of Kenya", "westlands", "Cuffed")
say_hi("Gee", 18, "Qatar School of Aviation", "Kenya airways", "cuffed")

def say_hi(name, age, work,study):
    print("Hello " + name + ", you are ! " + str(age) + ", You work in! " +
          work + ", Studied at " + study)
say_hi("Dunnieboy", 22, "Westlands", "The Technical University of Kenya")
say_hi("Geestar", 18, "Kenya airways", "Qatar School of Aviation")

#Do revision here Dee !!You are Terrible

#THE DICTIONARY

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Nov": "November",
    "Dec": "December",
}
print(monthConversions.get("Nov"))

