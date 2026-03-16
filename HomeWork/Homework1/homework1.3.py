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
               