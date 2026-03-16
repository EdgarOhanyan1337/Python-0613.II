import math
a = int((input("Введите первое число которое не равно 0: ")))
b = int((input("Введите второе число ")))
c = int((input("Введите третье число ")))
d = b*b - 4*a*c
if a == 0:
    print("Первое число равно 0") 
    exit()
if d < 0:
    print("Корней нет")
elif d == 0:
    x = -b / (2*a)
    print("Корень один")
    print("x = ", x)
else:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Корней два")
    print("x1 = ", x1)
    print("x2 = ", x2)

