"""
Working with lists in python
#Using Functions..........
min(friends)
max(friends)
len(friends)
friends(seq)
#using METHODS.............
friends.count()
friends.extend()
friends.append()
friends.index()
friends.insert()
friends.remove()
friends.reverse()
friends.sort()
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
working with list METHODS
"""
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Dunnie", "Eddy", "Hermon", "Geestar", "Dee"]

print(friends, lucky_numbers)
#use the extend function to add the second list
friends.extend(lucky_numbers)
print(friends)

#use the append function to add an individual list
friends.append("Creed")
print(friends)

#use insert function to add value in the middle of a list
friends.insert(1, "Emily")
print(friends)

#use remove function to delete a value from a list
friends.remove("Dee")
print(friends)

#use clear function to delete every value in a list
#friends.clear()
#print(friends)

#use of pop function to remove the last value in a list
#friends.pop()
#print(friends)

#use of index to determine whether a value exists in a list
print(friends.index("Hermon"))

#use of count function to know the number of items sharing the same value in a list
print(friends.count("Geestar"))

#use of sort function to arrange the values in a list
#friends.sort()
#print(friends.sort())
print(" ")
#lucky_numbers.sort()
#print(lucky_numbers)

#use of reverse function
lucky_numbers.reverse
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

#working with list FUNCTIONS
name = ["Dunnie", "Eddy", "Hermon", "Geestar", "Dee", "Geestar"]
print(max(name)) # returns the largets value
print(min(name)) # returns the minimum value
print(len(name)) # returns number of elements in a list



