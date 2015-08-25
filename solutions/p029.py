#
# Solution to Project Euler Problem 29
#
# Distinct terms in a generated sequence
#

terms = set()
for a in range(2, 101):
    for b in range(2, 101):
        terms.add(a ** b)

print(len(terms))
