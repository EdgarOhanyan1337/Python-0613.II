'''while True:    #Mutqagrum

    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    while_popoxakan = True

    #gumarum hanum ban man
    print("Выберите операцию:")
    print("1 - Сложение (+)")
    print("2 - Вычитание (-)")
    print("3 - Умножение (*)")
    print("4 - Деление (/)")
    print("5 - Возведение в степень (**)")
    print("6 - Остаток от деления (%)")

    choice = input("Введите номер операции: ")
    match choice:
        case "1":
            print("Результат:", x + y)
        case "2":
            print("Результат:", x - y)
        case "3":
            print("Результат:", x * y)
        case "4":
            if y != 0:
                print("Результат:", x / y)
            else:
                print("Ошибка: деление на ноль!")
        case "5":
            print("Результат:", x ** y)
        case "6":
            if y != 0:
                print("Результат:", x % y)
            else:
                print("Ошибка: деление на ноль!")
        case _:
            print("Неверный выбор операции") '''

x = int(input('mutqagreq tiv'))
if x>100:
    
    y = x // 100
    z = (x % 100)//10
    w = x % 10 
    print(y)
    print(z)
    print(w)
    print(y+z+w)
else:
    print('ЧИСЛО МАЛЕНЬКОЕ ТУПОЕ ТЫ СУЩЕСТВО КОТОРОЕ НИЧЕГО НЕ ПОНИМАЕТ')

