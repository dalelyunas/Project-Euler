#
# Solution to Project Euler Problem 26
#
# d < 1000 for 1/d which has the longest recurring cycle
#

import decimal
from decimal import Decimal

decimal.getcontext().prec = 2000


def recurring_cycle(d):
    dec = str(Decimal(Decimal(1) / Decimal(d)))[2:].lstrip("0")
    for i in range(0, len(dec)):
        for j in range(i, len(dec)):
            if dec[i:j] != "" and dec[i:j] == dec[j:j * 2 - i]:
                    return dec[i:j]


def check_denoms():
    longest = 0
    longestpattern = 0
    for i in range(2, 1000):
        pattern = recurring_cycle(i)
        if pattern is not None:
            if len(pattern) > longest:
                longest = len(pattern)
                longestpattern = i

    return longestpattern

print(check_denoms())
