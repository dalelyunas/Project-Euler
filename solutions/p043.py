#
# Solution to Project Euler Problem 43
#

import itertools


def is_sub_divis(num):
    num = str(num)
    return (int(num[1:4]) % 2 == 0 and
            int(num[2:5]) % 3 == 0 and
            int(num[3:6]) % 5 == 0 and
            int(num[4:7]) % 7 == 0 and
            int(num[5:8]) % 11 == 0 and
            int(num[6:9]) % 13 == 0 and
            int(num[7:10]) % 17 == 0)


to_check = itertools.permutations(['0', '1', '2', '3', '4',
                                   '5', '6', '7', '8', '9'])

sum_ = 0
for perm in to_check:
    num = int(''.join(perm))
    if is_sub_divis(num):
        sum_ += num

print(sum_)
