#
# Solution to Project Euler Problem 24
#
# millionth lexographic permutation of 0123456789
#

import itertools

print(list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))[999999])
