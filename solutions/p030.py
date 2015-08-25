#
# Solution to Project Euler Problem 30
#
# Sum of all the numbers that can be written as the sum
# of fifth powers of their digits
#

total = 0
for i in range(2, 354294):
    string = str(i)
    num = sum([int(x) ** 5 for x in str(i)])
    if num == i:
        total += num

print(total)
