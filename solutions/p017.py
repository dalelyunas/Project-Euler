#
# Solution to Project Euler Problem 17
#
# number of letters in all numbers from 1 to 1000
#


# Gets the number of letters in numbers less than 1000
def letters_in_number(num):
    ones_digit = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3]
    special_tens = [0, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tens_digit = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
    hundred = 7

    if num >= 100:
        num = str(num)
        first = hundred + ones_digit[int(num[0])]
        if int(num[1:]) >= 20:
            second = tens_digit[int(num[1])]
            third = ones_digit[int(num[2])]
        elif int(num[1:]) > 10:
            second = special_tens[int(num[2])]
            third = 0
        else:
            second = ones_digit[int(num[2])]
            third = 0
        return first + second + third + 3

    if num >= 20:
        num = str(num)
        return tens_digit[int(num[0])] + ones_digit[int(num[1])]

    if num > 10:
        num = str(num)
        return special_tens[int(num[1])]

    else:
        return ones_digit[int(num)]


total = 0
for i in range(1, 1000):
    total += letters_in_number(i)

total += 11
print(total)
