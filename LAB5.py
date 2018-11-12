a = int(input('Введть натуральне число:'))
k = ''
while a > 0:
    y = str(a % 2)
    k += y
    a = int(a / 2)
x = k[::-1]
print(x)
print(k)
print(int(k, 2))
input('press ENTER to exit')
