#
# Solution to Project Euler Problem 16
#
# Sum of the digits of 2^1000
#

total = sum(map(int, str(2 ** 1000)))
print(total)
