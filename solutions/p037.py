#
# Solution to Project Euler Problem 37
#

import utils


def truncatable(num):
    num = str(num)
    temp_num = str(num)
    for i in range(0, len(num) - 1):
        temp_num = temp_num[1:]
        if not utils.is_prime(int(temp_num)):
            return False

    for i in range(0, len(num) - 1):
        num = num[:-1]
        if not utils.is_prime(int(num)):
            return False

    return True


primes_so_far = []
for prime in utils.sieve_of_eratosthenes(1000000)[4:]:
    if truncatable(prime):
        primes_so_far.append(prime)

print(sum(primes_so_far))
