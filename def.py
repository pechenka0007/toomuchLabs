from math import atan, sin, fabs, exp, pi

a, b, n = int(input("A:")), int(input("B:")), int(input("N:"))
h = (b - a) / n
s = 0
n = fabs(n)
n = int(n)


def integ(f, a, b):
    s = (f(a) + f(b)) / 2
    for i in range(n - 1):
        s += (f(a + i * h)) ** 2
    return s


def arctg2(x):
    return atan(x) ** 2


def sinus2(x):
    return sin(exp(1) ** (10 * x))


print(integ(arctg2, a, b) + integ(sinus2, 0, pi))
