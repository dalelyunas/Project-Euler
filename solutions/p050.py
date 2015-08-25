#
# Solution to Project Euler Problem 50
#

import utils


prime_list = [x for x in utils.sieve_of_eratosthenes(1000000) if x < 100000]
max_ = 0
for i in range(0, len(prime_list)):
    for j in range(i + 1, len(prime_list)):
        if sum(prime_list[i:j]) > 1000000:
            break
        if utils.is_prime(sum(prime_list[i:j])) and j - i > max_:
            max_ = j - i
            print(str(sum(prime_list[i:j])) + ', ' + str(max_))
