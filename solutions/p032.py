#
# Solution to Project Euler Problem 32
#

products = []

total = 0
for i in range(0, 100):
    for j in range(0, 10000):
        num = i * j
        if len(str(num)) > 4:
            break
        if "".join(sorted(str(i) + str(j) + str(num))) == "123456789":
            if num not in products:
                products.append(num)
                print(num)
                total += num

print(total)
