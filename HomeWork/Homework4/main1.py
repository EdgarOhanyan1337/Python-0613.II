List_1=[[3,5,8,-9,6],
        [-1,2,9,0,-8], 
        [6,-7,9,0,3],
        [-6,8,9,0,4],
        [-15,0,6,9,7]]

#gumarum
s = 0
i = 0
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

#min ev index
min_val = List_1[0][0]
i = 0
while i < len(List_1):
    j = 0
    while j < len(List_1[i]):
        if List_1[i][j] < min_val:
            min_val = List_1[i][j]
            min_index = i+1,j+1 #inatu em grel +1 vor aveli lav haskanali lini
        j += 1
    i += 1
print(f"{min_val} ev indexy {min_index}")


#max ev index
max_val = List_1[0][0]
i = 0
max_index = 0
while i < len(List_1):
    j = 0
    while j < len(List_1[i]):
        if List_1[i][j] > max_val:
            max_val = List_1[i][j]
            max_index = i+1,j+1
        j += 1
    i += 1
print(f"{max_val} ev indexy {max_index}")

#drakan bacasakan ev zroyakan
drakan = 0
bacasakan = 0
zroyakan = 0
i = 0
while i < len(List_1):
    j = 0
    while j < len(List_1[i]):
        if List_1[i][j] > 0:
            drakan += 1
        elif List_1[i][j] < 0:
            bacasakan += 1
        else:
            zroyakan += 1
        j += 1
    i += 1
print(drakan)
print(bacasakan)
print(zroyakan)


#sortingy eli chhaskaca vonc


#zuyg ev kent indexneri gumary
i = 0
while i < len(List_1):
    j = 0
    while j < len(List_1[i]):
        if List_1[i][j] % 2 == 0:
            print(List_1[i][j])
        j += 1
    i += 1
