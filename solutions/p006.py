#
# Solution to Project Euler Problem 6
#
# Difference between the sum of the squares and the square of the sum of the
# first 100 natural numbers
#


def sum_and_squared_sum():
    num = 0
    square = 0
    for i in range(1, 101):
        square += i * i
        num += i

    return num * num - square


if __name__ == "__main__":
    print sum_and_squared_sum()
