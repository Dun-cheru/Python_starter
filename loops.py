"""
Woorking with loops in python
#First values will be assigned
#Secondly, all the statements in the body of the loop are executed with the same value
#Thirdly, once step 2 is completed the variable is assigned the next value in the sequence and the 
second step is repeated
Finally, it continues till all the values in the sequence are assigned in the variable and
processed
"""
num = 2

for a in range (1, 6):  # in place of a you can use any value or letter there 1.e name, school.
    print(num * a)
    
print(" ")# printing space to show where a code has ended
    
#python example to find the sum of 10 numbers:
sum = 0
for Dee in range(1, 11):
    sum+=Dee
    print(sum)

print(" ")

#python nested for loops:
for i in range(1, 6):
    for j in range (1, i + 1):
        print(i,)
    print

print(" ")

#Python break statements
"""
"""
number = 0
for number in range(10):
    number = number + 1
    if number == 5:
        break # Break here
    print("Number is " + str(number))
print("Out of loop")

print(" ")

#using the Python pass statement
"""
The PASS statement used below tell the program to disregard the condition and continues to run
"""
number = 0
for number in range(10):
    number = number + 1
    if number == 5:
        pass # pass here
    print("Number is " + str(number))
print("Out of loop!")



























