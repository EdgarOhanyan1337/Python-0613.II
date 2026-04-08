# 1. Հայտարարել թիվ և ստուգել այն կենտ է, թե զույգ
number = 10
if number % 2 == 0:
    print(f"{number}-ը զույգ է")
else:
    print(f"{number}-ը կենտ է")

print("-" * 20)

# 2. Հայտարարել թիվ, և որոշել այն դրական է, բացասական, թե զրո
val = -5
if val > 0:
    print(f"{val}-ը դրական թիվ է")
elif val < 0:
    print(f"{val}-ը բացասական թիվ է")
else:
    print("Թիվը զրո է")

print("-" * 20)

# 3. Հայտարարել երկու թիվ, որոշել որն է նրանցից մեծը
num1 = 15
num2 = 25
if num1 > num2:
    print(f"Մեծ թիվը {num1}-ն է")
elif num2 > num1:
    print(f"Մեծ թիվը {num2}-ն է")
else:
    print("Թվերը հավասար են")
