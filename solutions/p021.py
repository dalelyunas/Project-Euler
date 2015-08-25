#
# Solution to Project Euler Problem 21
#
# All Amicable pairs under 10000
#


def divisor_sum(num):
    total = 0
    for i in range(1, num / 2 + 1):
        if num % i == 0:
            total += i

    return total


total = 0
for i in range(1, 10000):
    if i == divisor_sum(divisor_sum(i)):
        if i == divisor_sum(i):
            total += 0
        else:
            total += i

print(total)
