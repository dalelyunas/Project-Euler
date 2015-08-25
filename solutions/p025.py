#
# Solution to Project Euler Problem 25
#
# Index of the first term in the fib sequence to contain 1000 digits
#


def fib_list(limit):
    temp_list = [1, 1]

    while True:
        n_val = temp_list[len(temp_list) - 1] + temp_list[len(temp_list) - 2]
        temp_list.append(n_val)
        if len(str(temp_list[len(temp_list) - 1])) == limit:
            return len(temp_list)

print(fib_list(1000))
