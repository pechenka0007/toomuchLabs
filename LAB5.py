n1 = int(input('N:'))
n2 = 0
while n1 > 0:
    if n2 != 0:
        n2 = int(n2) << 1
    n2 += int(n1 % 2)
    n1 = n1 >> 1
print(n2)
