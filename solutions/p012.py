#
# Solution to Project Euler Problem 12
#
# What is the value of the first triangle number with 500 divisors
#

import math
from collections import Counter
import utils


# Finds the number of divisors of the number
def num_divisors(num):
    primes = utils.sieve_of_eratosthenes(int(math.ceil(math.sqrt(num))))
    factors = []
    prime_counter = 0
    while num != 1:
        if prime_counter > len(primes) - 1:
            if num % 2 != 0 and num > 3 and utils.is_prime(num, 10):
                factors.append(num)
                break
            else:
                print("fail")
                break
        if num % primes[prime_counter] == 0:
            num /= primes[prime_counter]
            factors.append(primes[prime_counter])
        else:
            prime_counter += 1

    c = Counter(factors)

    product = 1

    for key, value in c.iteritems():
        value += 1
        product *= value

    return product


def generate_triangles():
    next_triangle = 55
    triangle_iter = 10
    while num_divisors(next_triangle) < 500:
        next_triangle = triangle_iter * (triangle_iter + 1) / 2
        triangle_iter += 1

    return next_triangle


if __name__ == "__main__":
    print(generate_triangles())
