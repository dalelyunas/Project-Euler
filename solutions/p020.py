#
# Solution to Project Euler Problem 20
#
# Sum of the digits of 100!
#

import math

print(sum(map(int, str(math.factorial(100)))))
