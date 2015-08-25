#
# Solution to Project Euler Problem 31
#

coin_values = [1, 2, 5, 10, 20, 50, 100, 200]


def coin_combinations(values, accumulator):
    if sum(accumulator) == 200:
        return 1

    local_total = 0
    last = accumulator[-1] if accumulator else values[0]
    for i in range(0, len(values)):
        if sum(accumulator) <= 200 and last <= values[i]:
            local_total += coin_combinations(values, accumulator + [values[i]])

    return local_total

print(coin_combinations(coin_values, []))
