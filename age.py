from datetime import date
d = int(input("Enter day: "))
m = int(input("Enter month: "))
y = int(input("Enter year: "))
date_ = date(y, m, d)
today = date.today()
years = (today - date_).days // 365
print(f"{years} years")
input()