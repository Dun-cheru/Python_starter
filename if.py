#using if to determine students grade
num = float(input("Enter students marks to check grade: "))
if num >=70 and num <= 100:
    print("Grade A")
elif num >=60 and num <= 69:
    print("Grade B")
elif num >= 50 and num <= 59:
    print("Grade C")
elif num >=40 and num <= 49:
    print("Grade D")
elif num >= 0 and num <=39:
    print("Fail")
else:
    print("INVALID NUMBER")

# using while for endless loop
while (True):
    name = ("Dunnieboy", "Geestar", "Hermon")
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9,0]
    print(name, num)

#Remove the comments(""") to make the endless loop work
