"""
Container where you can store different values
Builtin Functions
>>len(coordinate)
>>
"""
coordinates = (4, 5)
#Tuples cannot be modified
print(coordinates[0])
#differemce between a tuple and a list is that a list can be modified
#For a list we use square brackets but for a tuple we use paranthesis

coordinate = [44, 5]
coordinate[1] = (7)
print(coordinate[1])
del coordinates;
