#
# Solution to Project Euler Problem 35
#

import utils


def prime_rots(num):
    num = str(num)
    rotations = []
    rotated = num[-1] + num[0:-1]
    rotations.append(rotated)
    while rotated != num:
        rotated = rotated[-1] + rotated[0:-1]
        rotations.append(rotated)

    for num in rotations:
        if not utils.is_prime(int(num)):
            return False

    return True


total = 0
for i in range(0, 1000000):
    if prime_rots(i):
        total += 1

print(total)
