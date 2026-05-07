List_1 = [1,490,23940,238,100,-3948,-345,12,-58,-228,67,8,999]
i=0
#gumarum
sum = 0
while i<len(List_1):
    sum += List_1[i]
    i+=1
print(sum)

#bazmapatkum
i = 0
bazm = 1
while i<len(List_1):
    bazm *= List_1[i]
    i+=1
print(bazm)

#max
i = 0
max_val = List_1[0]
while i<len(List_1):
    if List_1[i] > max_val:
        max_val = List_1[i]
    i+=1
print(max_val)


#min
i = 0
min_val = List_1[0]
while i<len(List_1):
    if List_1[i] < min_val:
        min_val = List_1[i]
    i+=1
print(min_val)


#max index
i = 0
max_val = List_1[0]
max_idx = 0
while i < len(List_1):
    if List_1[i] > max_val:
        max_val = List_1[i]
        max_idx = i
    i += 1
print(f"tivy {max_val} kargahamary {max_idx+1}")


#min index
i = 0
min_val = List_1[0]
min_idx = 0
while i < len(List_1):
    if List_1[i] < min_val:
        min_val = List_1[i]
        min_idx = i
    i += 1
print(f"tivy {min_val} kargahamary {min_idx+1}")


#sort
i = 0 
drakan=0
bacasakan=0
zroyakan=0
while i<len(List_1):
    if List_1[i]>0:
        drakan+=1
    elif List_1[i]<0:
        bacasakan+=1
    else:
        zroyakan+=1
    i+=1
print(drakan)
print(bacasakan)
print(zroyakan) #zroyakan chka vorovhetev bazmapatkumy animast kliner

#sort-y chhaskaca vonc petqa anem (maybe bubble sort petqa anei idk)

#9. Հաշվել տրված ցուցակի զույգ ինդեքս ունեցող տարրերի գումարը և կենտ ինդեք ունեցող տարրերի գումարը:

i=0 
sum_z = 0 
sum_k = 0
while i<len(List_1):
    if i%2 == 0:
        sum_z += List_1[i]
    else:
        sum_k += List_1[i]
    i+=1
print(sum_z)
print(sum_k)