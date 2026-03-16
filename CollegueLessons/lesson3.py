from unittest import case

'''x = int(input("Enter a number of months: "))
y = int(input("Enter a number of month(season): "))
a = int(input("Enter a number of month: "))
b = int(input("Enter a number of month(season): ")) 
match x:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case 13:
        print("Error")
    case _:
        print("Error") 

match y:
    case 1|2|12:
        print("Winter")
    case 3|4|5:
        print("Spring")
    case 6|7|8:
        print("Summer")
    case 9|10|11:
        print("Autumn")
    case _:
        print("Error")

if a == 1:
    print("January")
elif a == 2:
    print("February")
elif a == 3:
    print("March")
elif a == 4:
    print("April")
elif a == 5:
    print("May")
elif a == 6:
    print("June")
elif a == 7:
    print("July")
elif a == 8:
    print("August")
elif a == 9:
    print("September")
elif a == 10:
    print("October")
elif a == 11:
    print("November")
elif a == 12:
    print("December")
else:
    print("Error")

if b == 1 or b == 2 or b == 12:
    print("Winter")
elif b == 3 or b == 4 or b == 5:
    print("Spring")
elif b == 6 or b == 7 or b == 8:
    print("Summer")
elif b == 9 or b == 10 or b == 11:
    print("Autumn")
else:
    print("Error")'''

x = int(input("A dot in x: "))
y = int(input("A dot in y: "))
match (x, y):
    case (0, 0):
        print("The dot is in the center")
    case (0, _):
        print("The dot is on the y-axis")
    case (_, 0):
        print("The dot is on the x-axis")
    case (x, y) if x > 0 and y > 0:
        print("The dot is in the first quarter")
    case (x, y) if x < 0 and y > 0:
        print("The dot is in the second quarter")
    case (x, y) if x < 0 and y < 0:
        print("The dot is in the third quarter")
    case (x, y) if x > 0 and y < 0:
        print("The dot is in the fourth quarter")
               