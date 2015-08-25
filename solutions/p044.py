#
# Solution to Project Euler Problem 44
#

import math


def calc_pent(n):
    return n * (3 * n - 1) / 2


def is_pent(n):
    return (math.sqrt(24 * n + 1) + 1) % 6 == 0

pent_not_found = True
n = 1
while pent_not_found:
    next_pent = calc_pent(n)

    for i in range(1, n - 1):
        if (is_pent(next_pent + calc_pent(i)) and
                is_pent(abs(next_pent - calc_pent(i)))):
            pent_not_found = False
            print(next_pent - calc_pent(i))
    n += 1
