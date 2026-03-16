a = int((input("Введите первое число: ")))
b = int((input("Введите второе число: ")))
c = int((input("Введите третье число: ")))
d = int((input("Введите четвертое число: ")))

match a, b, c, d:
    case a, b, c, d if a == b == c == d:
        print("Все числа равны")
    case a, b, c,d if a<b and a<c and a<d:
        print("Первое число самое маленькое")
    case a, b, c,d if b<a and b<c and b<d:
        print("Второе число самое маленькое")
    case a, b, c,d if c<a and c<b and c<d:
        print("Третье число самое маленькое")
    case a, b, c,d if d<a and d<b and d<c:
        print("Четвертое число самое маленькое")
    case _:
        print("Есть несколько чисел которые равны наименьшему числу")

    