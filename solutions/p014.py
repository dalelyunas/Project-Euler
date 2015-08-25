#
# Solution to Project Euler Problem 14
#
# Longest Collatz sequence starting under 1000000
#


# Less optimal function (too many function calls) , but better readability
def sequence_length(start):
    length = 0
    while start != 1:
        if start % 2 == 0:
            start /= 2
            length += 1
        else:
            start = 3 * start + 1
            length += 1

    return length


if __name__ == "__main__":
    longest = 0
    longest_value = 0
    for i in range(1, 1000000):
        s = sequence_length(i)
        if s > longest:
            longest = s
            longest_value = i

    print(longest_value)
