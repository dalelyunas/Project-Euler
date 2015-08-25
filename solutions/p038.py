#
# Solution to Project Euler Problem 38
#


def pan_conc_prod(num):
    largest = 0
    total = ""
    i = 1
    while len(total) < 9:
        total += str(num * i)
        if len(total) == 9:
            if sorted(total) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if int(total) > largest:
                    largest = int(total)
        i += 1

    return (largest, largest != 0)


max_pan = 0
for i in range(1, 99999):
    if pan_conc_prod(i)[1]:
        if pan_conc_prod(i)[0] > max_pan:
            max_pan = pan_conc_prod(i)[0]

print(max_pan)
