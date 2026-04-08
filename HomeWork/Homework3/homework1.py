for i in range(5):
    print("*****")

print()

x = 1
while x < 6:
    print(str(x) * 4)
    x+=1

print()

for i in range(5):
    print(12345)

print()

q=1
while q < 6:
    print("*"*q)
    q+=1

print()

w=1
while w < 6:
    print(str(w) * w)
    w += 1

print()

e = 1
tox = ""
while e < 6:
    tox += str(e)
    print(tox)
    e += 1

print()

q=5
while q > 0:
    print("*"*q)
    q-=1

print()


z = 1
while z < 6:
    print(str(z) * (6 - z))
    z += 1

print()

k = 5
full = "12345"
while k > 0:
    print(full[:k])
    k -= 1

print()

r = 1

while r < 6:
    print(" " * (5 - r) + "*" * r)
    r += 1
print()

# 1, 22, 333, 4444, 55555 (справа)
r1 = 1
while r1 < 6:
    print(" " * (5 - r1) + str(r1) * r1)
    r1 += 1

print()

# 1, 12, 123, 1234, 12345 (справа)
r2 = 1
res_r = ""
while r2 < 6:
    res_r += str(r2)
    print(" " * (5 - r2) + res_r)
    r2 += 1

print()
