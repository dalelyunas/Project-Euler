#
# Solution to Project Euler Problem 41
#

import utils


def is_9_pan(n):
    test_list = [x for x in range(1, len(str(n)) + 1)]
    sort_list = [int(x) for x in str(n)]
    sort_list.sort()
    if sort_list == test_list:
        return True

    return False


primes = utils.sieve_of_eratosthenes(8000000)
largest = 0
i = 1000
while primes[i] <= 7654321 and i < len(primes):
    if is_9_pan(primes[i]):
        if primes[i] > largest:
            largest = primes[i]
    i += 1

print(largest)
