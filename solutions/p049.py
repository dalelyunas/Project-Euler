#
# Solution to Project Euler Problem 49
#

import utils
import itertools


def equal_gap(one, two, three):
    return two - one == three - two


def check_perms(n):
    perms = [int(''.join(p)) for p in itertools.permutations(str(n), 4)]
    perms = [perm for perm in perms if utils.is_prime(perm) and perm >= 1000]
    for i in range(0, len(perms)):
        for j in range(i + 1, len(perms)):
            for h in range(j + 1, len(perms)):
                if (perms[i] != perms[j] != perms[h] and
                        equal_gap(perms[i], perms[j], perms[h])):
                        return (str(perms[i]) + ', ' +
                                str(perms[j]) + ', ' + str(perms[h]))


primes = utils.sieve_of_eratosthenes(10000)
lower_index = 0
upper_index = len(primes)
for i in range(0, len(primes)):
    if primes[i] > 1000:
        lower_index = i - 1
        break

for i in range(lower_index, upper_index):
    check = check_perms(primes[i])
    if check is not None:
        print(check)
