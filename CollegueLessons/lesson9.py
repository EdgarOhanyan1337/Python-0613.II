import math

#grel funckcia vory hashhvum e trvac tvi xonarhardy ev hashvel trvac 5 tveri xonarhardy

'''number_list = []
i = 0

while i<5:
    i+=1
    user = int(input("mutqagreq tiv"))
    number_list.append(user)

print(number_list)

def get_third(n):
    return n ** 3

for i in range(len(number_list)):
    number_list[i] = get_third(number_list[i])

print(number_list)

'''

a = int(input("mutqagreq tiv"))
b = int(input("mutqagreq tiv"))


def sign(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0


y=sign(a) + sign(b)
print(y)