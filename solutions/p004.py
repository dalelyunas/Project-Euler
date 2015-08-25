#
# Solution for Project Euler Problem 4
#
# Largest palindrome made from the product of two 3 digit numbers
#
import math


def num_is_palindrome(num):
    digits = []
    while num >= 10:
        digits.append(num % 10)
        num /= 10

    digits.append(num)
    if len(digits) % 2 != 0:
        del digits[int(math.floor(len(digits) / 2))]

    for i in range(0, len(digits) / 2):
        if digits[i] != digits[len(digits) - 1 - i]:
            return False
    return True


def iter_over_combos():
    l_palindrome = 0

    for i in range(100, 999):
        for j in range(100, 999):
            if num_is_palindrome(i * j) and i * j > l_palindrome:
                l_palindrome = i * j

    return l_palindrome


if __name__ == "__main__":
    print(iter_over_combos())
