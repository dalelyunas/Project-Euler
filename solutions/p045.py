#
# Solution to Project Euler Problem 45
#

import math


def is_pent(n):
    return (math.sqrt(24 * n + 1) + 1) % 6 == 0


def is_hex(n):
    return (math.sqrt(8 * n + 1) + 1) % 4 == 0

num_not_found = True
n = 286
while num_not_found:
    tri = n * (n + 1) / 2
    if is_pent(tri) and is_hex(tri):
        print(tri)
        num_not_found = False
    n += 1
