#
# Solution to Project Euler Problem 36
#

total = 0
for i in range(0, 1000000):
    if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[2:][::-1]:
        total += i

print(total)
