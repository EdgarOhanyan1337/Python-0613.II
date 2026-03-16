birth_year = int(input("Enter your birth year(xxxx format): "))
birth_month = int(input("Enter your birth month(xx format): "))
current_year = int(input("Enter current year(xxxx format): "))
current_month = int(input("Enter current month(xx format): "))

if birth_month <= 0 or birth_month > 12:
    print("Bruh you can't be born in month 0 or month bigger than 12")
    exit()
if current_month <= 0 or current_month > 12:
    print("Bruh you can't be live in month 0 or month bigger than 12")
    exit()
year = current_year - birth_year
month = current_month - birth_month

if birth_year > current_year:
    print("Bruh you can't be born in future")
    exit()
if birth_month > current_month:
    print(f"You are {year - 1} years and {month + 12} months old")
else:
    print(f"You are {year} years and {month} months old")

if birth_year == current_year and birth_month == current_month:
    print("Bruh you born this year, you are 0 years old")

