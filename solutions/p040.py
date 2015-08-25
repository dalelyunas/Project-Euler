#
# Solution to Project Euler Problem 40
#

digitss = 0

d = ''
for i in range(1, 200000):
    d += str(i)

total = 1
for i in range(1, 6):
    total *= int(d[int('9' * i)])

print(total)
