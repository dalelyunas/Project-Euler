#
# Solution to Project Euler Problem 46
#

import utils


def fits_gold(n):
    i = 1
    while i < n:
        s = 1
        if utils.is_prime(i):
            while s ** 2 < n:
                if i + 2 * s ** 2 == n:
                    return True
                s += 1
        i += 1
    return False

not_found = True
i = 9
while not_found:
    if not utils.is_prime(i) and not fits_gold(i):
        print(i)
        break
    i += 2
