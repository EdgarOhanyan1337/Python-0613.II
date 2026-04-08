import sys; sys.stdout.reconfigure(encoding='utf-8')


s1 = "Hello, world!"
if "world" in s1:
    print("1. 'world'-ը պարունակվում է տողում")
else:
    print("1. 'world'-ը չի պարունակվում տողում")

print()


s2 = "hello"
print(f"2. {s2} -> {s2.upper()}")

print()


s3 = "apple,banana,cherry"
fruits = s3.split(",")
print(f"3. Բաժանված ցուցակ՝ {fruits}")

print()


s4 = "I love Python"
res4 = s4.replace("Python", "programming")
print(f"4. Արդյունք՝ {res4}")

print()


s5 = " Hello "
print(f"5. '{s5}' -> '{s5.strip()}'")

print()

s6 = "Hello, world!"
if s6.startswith("Hello"):
    print("6. Տողը սկսվում է 'Hello' բառով")
else:
    print("6. Տողը չի սկսվում 'Hello' բառով")

print()

s7 = "level"
if s7 == s7[::-1]:
    print(f"7. '{s7}'-ը պալինդրոմ է")
else:
    print(f"7. '{s7}'-ը պալինդրոմ չէ")
