#
# Solution to Project Euler Problem 33
#

import utils


def is_curious(num, den):
    num_digits = [int(x) for x in sorted(str(num))]
    den_digits = [int(x) for x in sorted(str(den))]

    if num_digits[0] == den_digits[0] and num_digits[1] != den_digits[1]:
        if num_digits[0] != 0:
            return num / den == num_digits[1] / den_digits[1]

    if num_digits[1] == den_digits[1] and num_digits[0] != den_digits[0]:
        if num_digits[1] != 0 and den_digits[0] != 0:
            return num / den == num_digits[0] / den_digits[0]

    return False

total_num = 1
total_den = 1
for i in range(10, 100):
    for j in range(i, 100):
        if is_curious(i, j):
            total_den *= j
            total_num *= i
            print(str(i) + " / " + str(j))

total_den /= utils.gcd(total_num, total_den)
print(total_den)
