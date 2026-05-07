#erkchap zangvaci gumarom
List_1 = [[79,34,3299],[289,202,19],[9,88,884]]
s = 0
i = 0

#gumarum

while i < len(List_1):
    j = 0
    while j < len(List_1[i]):
        s += List_1[i][j]
        j += 1
    i += 1
print(s)

#bazmapatkum
bazm=1
i = 0
while i < len(List_1):
    j = 0
    while j < len(List_1[i]):
        bazm = List_1[i][j] * bazm 
        j += 1
    i += 1
print(bazm)

#max
max_val = List_1[0][0]
i = 0
while i < len(List_1):
    j = 0
    while j < len(List_1[i]):
        if List_1[i][j] > max_val:
            max_val = List_1[i][j]
        j += 1
    i += 1
print(max_val)

#min
min_val = List_1[0][0]
i = 0
while i < len(List_1):
    j = 0
    while j < len(List_1[i]):
        if List_1[i][j] < min_val:
            min_val = List_1[i][j]
        j += 1
    i += 1
print(min_val)
