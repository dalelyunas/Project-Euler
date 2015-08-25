#
# Solution to Project Euler Problem 7
#
# What is the 10001st prime
#


import utils

# Brute force using the sieve_of_eratosthenes
if __name__ == "__main__":
    primes = utils.sieve_of_eratosthenes(200000)
    print(primes[10000])
