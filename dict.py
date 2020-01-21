#Using the Dictionary
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
print(monthConversions.items())
for m in monthConversions.items():
    print(m)

print(" ")

dict_ionary = {
    1: "Python",
    2: "C++",
    3: "C",
    4: "C#",
    5: "Java",
    6: "Ruby on Rails",
    7: "Pascal",
    8: "Z",
    9: "javascript",
    10: "Html & Css",
}
#Accessing dictionary values using their keys since we can't use index
print(dict_ionary[1])

#updating dictionary elements
dict_ionary[11] = "PHP" #insertion of new values 
dict_ionary[12] = "Bootstrap"
print(dict_ionary)

#We can use loop to return all the keys in the dictionary and their values too
print(dict_ionary.keys())
for x in dict_ionary.keys():
    print(dict_ionary[x])
    
#Deleting values/elements in a dictionary
del dict_ionary[10]
print(dict_ionary)

#dictionay functions
print(len(dict_ionary)) # prints the length of the dictionary elements
#print(str(dict_ionary) # produces a printable string representation of a dictionary
print(type(dict_ionary)) # returns the type of the passed variable

#Dictionary methods
"""
dict_ionary.clear()
dict_ionary.copy()
dict_ionary.fromkeys()
dict_ionary.get()
dict_ionary.items()
dict_ionary.keys()
dict_ionary.setdefault()
dict_ionary.update()
dict_ionary.value()
"""












