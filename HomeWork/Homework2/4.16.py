import math

circle_area = float(input("Введите площадь круга: "))
square_area = float(input("Введите площадь квадрата: "))

circle_radius = math.sqrt(circle_area / math.pi)
circle_diameter = 2 * circle_radius

square_side = math.sqrt(square_area)
square_diagonal = square_side * math.sqrt(2)

if circle_diameter <= square_side:
    print("а) Уместится ли круг в квадрате? Да")
else:
    print("а) Уместится ли круг в квадрате? Нет")

if square_diagonal <= circle_diameter:
    print("б) Уместится ли квадрат в круге? Да")
else:
    print("б) Уместится ли квадрат в круге? Нет")