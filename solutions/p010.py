#
# Solution to Project Euler Problem 10
#
# Sum of the primes below 2000000
#

import utils


def sum_of_primes():
    return sum(utils.sieve_of_eratosthenes(2000000))


if __name__ == "__main__":
    print(sum_of_primes())
