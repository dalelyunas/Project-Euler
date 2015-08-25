#
# Solution to Project Euler Problem 19
#
# Sundays on the first month in the twentieth century
#

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 3
month = 0
month_day = 1
year = 1901

sundays = 0
while year < 2001 and month < 13 and month_day < 32:
    day += 1
    month_day += 1

    if day > 7:
        day = 1

    if month > 11:
        month = 0
        year += 1

    if month_day > months[month]:
        month_day = 1
        month += 1

    if day == 1 and month_day == 1:
        sundays += 1

    if year % 4 == 0:
        months[1] = 29
    else:
        months[1] = 28

print(sundays)
