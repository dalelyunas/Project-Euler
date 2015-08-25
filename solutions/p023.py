#
# Solution to Project Euler Problem 23
#
# Sum of all positive integers that are not the sum of two
# abundant numbers
#


def divisor_sum(num):
    total = 0
    for i in range(1, num / 2 + 1):
        if num % i == 0:
            total += i

    return total

abund_nums = [x for x in range(0, 28124) if divisor_sum(x) > x]
all_sums = [False] * 28124

for i in range(0, len(abund_nums)):
    for j in range(i, len(abund_nums)):
        if abund_nums[i] + abund_nums[j] < 28124:
            all_sums[abund_nums[i] + abund_nums[j]] = True
        else:
            break

total = 0
all_sums_inc = 0
for i in range(1, 28124):
    if not all_sums[i]:
        total += i

print(total)
