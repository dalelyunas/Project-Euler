#
# Solution to Project Euler Problem 27
#
# coefficients of the quadratic that produces the maximum number of primes
#

import utils


def num_consec_primes(a, b):
    primes = 0
    n = 0
    while utils.is_prime(n * n + n * a + b):
        primes += 1
        n += 1

    return n


max = 0
a_x_b = 0
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        num_primes = num_consec_primes(a, b)
        if num_primes > max:
            max = num_primes
            a_x_b = a * b

print(max)
print(a_x_b)
