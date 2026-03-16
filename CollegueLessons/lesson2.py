import math

x = int(input('nermuceq dzer tivy'))
y = int(input('nermuceq dzer tivy'))
z = int(input('nermuceq dzer tivy'))

burger = False

if x<=0 or y<=0 or z<=0:
    print('nene ne poshlo')


elif x+y<z and y+z<x and z+x<y:
    print('nenen pepeshneyne')
    
else:
    burger = True             

if (x==y and y==z and x==z) and burger == True:
    print('havasarakoxm')

elif (x==y or y==z or x==z) and burger == True:
    print('havasarasrun')

else:
    print('voch havasarasrun voche havasarakoxm')
if burger == True:
    p = (x+y+z)/2
    area = math.sqrt(p*(p-x)*(p-y)*(p-z))
    print('your P is', p, 'your area is', area)


    

