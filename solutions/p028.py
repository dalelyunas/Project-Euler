#
# Solution to Project Euler Problem 28
#
# Sum of the diagonals of a 1001 x 1001 spiral
#

spacing_total = 1
spacing = spacing_total
sum = 0
sum_nums = 0
for i in range(0, 1002002):

    if spacing == 0:
        sum += i
        sum_nums += 1
        spacing = spacing_total
    else:
        spacing -= 1

    if sum_nums == 4:
        sum_nums = 0
        spacing_total += 2

print(sum)
