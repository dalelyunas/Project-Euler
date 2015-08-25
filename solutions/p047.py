#
# Solution to Project Euler Problem 47
#

import math
import utils


def prime_factors(num):
    primes = utils.sieve_of_eratosthenes(int(math.ceil(math.sqrt(num))) + 1)
    factors = set()
    prime_counter = 0
    while num != 1 and prime_counter < len(primes):
        if num % primes[prime_counter] == 0:
            num /= primes[prime_counter]
            factors.add(primes[prime_counter])
        else:
            prime_counter += 1
    if num != 1:
        factors.add(int(num))

    return factors


not_found = True
i = 100
row = 0
while not_found:
    if len(prime_factors(i)) >= 4:
        row += 1
    else:
        row = 0
    if row > 3:
        print(i - 3)
        not_found = False
    i += 1
