#
# Solution to Project Euler Problem 39
#

import math


def num_sols(p):
    num_trips = 0
    for a in range(1, p):
        for b in range(a + 1, p):
            c = math.sqrt(a ** 2 + b ** 2)
            if a + b + c == p:
                num_trips += 1

    return num_trips

print(num_sols(120))
largest = 0
largest_num = 0
for i in range(1, 1000):
    cur = num_sols(i)
    if cur > largest_num:
        largest = i
        largest_num = cur
        print(largest)

print(largest)
print(largest_num)
