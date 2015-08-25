# Utility functions for Project Euler Problems
import math
import operator as op


# Sieve that finds the first num primes
def sieve_of_eratosthenes(num):
    bool_list = [False] * 2 + [True] * (num - 2)
    primes = []

    for i in range(2, int(math.ceil(math.sqrt(num)))):
        if bool_list[i]:
            for j in range(i * i, num, i):
                bool_list[j] = False

    for i in range(0, len(bool_list)):
        if bool_list[i]:
            primes.append(i)

    return primes


def is_prime(num):
    num = abs(num)
    if num < 2:
        return False
    if num < 4:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True


def gcd(a, b):
    while b != 0:
        rem = a % b
        a = b
        b = rem

    return a


def ncr(n, r):
    r = min(r, n-r)
    if r == 0:
        return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom


def factorial(n):
    product = 1
    for i in range(2, n + 1):
        product *= i

    return product
