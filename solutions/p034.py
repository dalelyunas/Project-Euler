#
# Solution to Project Euler Problem 34
#

import utils

for i in range(3, 9999999):
    if sum([utils.factorial(int(x)) for x in str(i)]) == i:
        print(i)
