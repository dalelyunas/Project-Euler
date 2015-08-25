#
# Solution to Project Euler Problem 9
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#

import math


def pythag_triplet():
    for a in range(1, 1100):
        for b in range(1, 1100):
            c = math.sqrt(a * a + b * b)
            if a + b + c == 1000:
                return a * b * c


if __name__ == "__main__":
    print(pythag_triplet())
