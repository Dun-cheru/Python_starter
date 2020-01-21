"""
>>First the value in the variable is initialised
>>Secondly, the condition/expression in the while is evaluated.
If the condition is true, the condtrol enters in the body and executes
all the statements. If the condition passed results in false then the control exists
the body and then the control goes to next instruction after body of while.
>>Thirdly, in case the condition was true having completed all the statements, the
variable step second is followed. This process continues till the expression/condition
becomes false.
>>Finally Rest of code after is executed/
"""
i = 1
while i <= 10: # You can modify the values here i.e change 1 >=10:
    print("The value of i is",i)
    i = i + 1 # you can modify the values and change it to be greater than one
    #note if you modify the changes as per the comment you will have an output of infinite loop
print("Done with loop")
#Using while to make a guessing game
secret_word = "Dunnieboy"
guess = ""
while guess != secret_word:
    guess = input("Enter your Guess: ")
    
print(" ")

print("You win!")
#Using while, If, Else  to create a guessing game
secret_word = "snake"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
       guess = input("Enter your guess: ")
       guess_count += 1

    else:
        out_of_guesses = True
if out_of_guesses:
    print("out of Guesses, YOU LOSE!")
else:
    print("You win!")
    
print(" ")

a = 10

while a > 0:
    print ("Value of a is", a)
    a= a-1
print("Loop is completed")

print(" ")

num = 153
sum = 0

while num >0:
    r = num % 10
    sum +=r
    num = num/10
print(sum)
    
print(" ")

#Python continue statement
"""
..=>while <expr>:
.    <statement>
.    <statement>
.    break.......
.    <statement>.
.    <statement>.
.....continue   .
    <statement> .
    <statement> .
                .
<statement><=.....     
      
"""
a = 0

while a <= 5:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)
print("End of loop")






















