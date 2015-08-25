#
# Solution to Project Euler Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#

import utils
import math


# Naive first attempt by finding all the prime factors
def prime_factors(num):
    primes = utils.sieve_of_eratosthenes(int(math.ceil(math.sqrt(num))))
    factors = []
    prime_counter = 0
    while num != 1:
        if num % primes[prime_counter] == 0:
            num /= primes[prime_counter]
            factors.append(primes[prime_counter])
        else:
            prime_counter += 1

    return factors[len(factors) - 1]


# Brute force by finding the highest number the input is
# divisible by which = the highe#st prime factor
def better_solution(num):
    for i in range(2, num):
        if num % i == 0:
            num /= i
            print(i)
        i += 1


if __name__ == "__main__":
    print(prime_factors(600851475143))
    print(better_solution(600851475143))
