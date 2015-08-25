#
# Solution to Project Euler Problem 42
#


def word_value(word):
    return sum([ord(x) - 64 for x in word])


def is_triangle(num):
    i = 0
    while i * (i + 1) / 2 < num:
        i += 1
    if i * (i + 1) / 2 == num:
        return True
    return False


with open('p042_words.txt') as f:
    words = f.readlines()[0].replace('"', '').split(',')

    triangles = 0
    for word in words:
        if is_triangle(word_value(word)):
            triangles += 1

    print(triangles)
