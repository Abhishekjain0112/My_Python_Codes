day = 1
month = int(input("Enter The Month : "))
year = int(input("Enter The Year"))
totalday = 28

monthof31 = (1, 3, 5, 7, 8, 10, 12)
if month in monthof31:
    totalday = 31
else:
    totalday = 30

century_digits = int(year / 100)
year_digits = int(year % (century_digits * 10))
value = year_digits + year_digits // 4

if century_digits == 18:
    value += 3

elif century_digits == 20:
    value += 6

if month == 1 and year % 4 != 0:
    value += 1
elif month == 2 and year % 4 == 0:
    value += 3
    totalday = 29
elif month == 2 and year % 4 != 0:
    value += 4
    totalday = 28
elif month == 3 or month == 11:
    value += 4
elif month == 5:
    value += 2
elif month == 6:
    value += 5
elif month == 8:
    value += 3

elif month == 10:
    value += 1


elif month == 3 or month == 11:
    value += 6

value = (value + day) % 7

weekday_dictionary = {
    0: 'Saturday',
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
}

print("S   M   T   W   T   F   S")

count = 0
for i in range(1, value):
    print("    ", end="")

count = value

for i in range(1, totalday + 1):
    if i in range(1, 10):
        print(i, end="   ")
    else:
        print(i, end="  ")

    count = count + 1
    if count > 7:
        count = 1
        print(" ")

