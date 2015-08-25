#
# Solution to Project Euler Problem 22
#
# Sum of name scores in a file
#

import string


def word_score(word):
    word = word.lower()
    return sum([string.lowercase.index(x) + 1 for x in word])

print(word_score("C"))
print(word_score("COLIN"))
with open("p022_names.txt") as f:
    lines = f.readlines()
    lines = lines[0].split(",")
    lines.sort()
    lines = [w.replace("\"", "") for w in lines]

    total = 0
    for i in range(0, len(lines)):
        total += word_score(lines[i]) * (i + 1)

    print(total)
