def check_parz(number):
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

number = int(input("mutqagreq tiv: "))
print(check_parz(number))

# grel hashvel arajin n parz tvery
n = int(input("mutqagreq qanaky: "))

def print_parz(count):
    found = 0
    j = 2
    while found < count:
        if check_parz(j):
            print(j)
            found += 1
        j+=1

print_parz(n)