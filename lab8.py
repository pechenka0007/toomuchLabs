import random


def sort(nlist, k):
    for i in range(0, len(nlist) - 1):
        for j in range(0, len(nlist) - 1 - i):
            if nlist[j][k] < nlist[j + 1][k]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
    return nlist


n = int(input('N:'))
ma1 = [[random.randrange(0, 10) for i in range(n)] for j in range(n)]


def matrgen(nlist):
    for i in range(len(nlist)):
        nlist[i][i] = nlist[i][i]
        print(nlist[i])


print('ma1:')
matrgen(ma1)
ma2 = []


def matrsort():
    for i in range(n):
        sort(ma1, i)
        if i >= 1:
            line = 1
            for k in range(len(ma1) - 1):
                if ma1[0][i] > ma2[i - 1][i - 1]:
                    ma1[0][i], ma1[line][i] = ma1[line][i], ma1[0][i]
                    line += 1
        ma2.append(ma1.pop(0))


def err():
    for i in range(n - 1):
        if ma2[i + 1][i + 1] > ma2[i][i]:
            print('Матрицю відсортувати неможливо')
            break


def call():
    diag = []
    matrsort()
    err()
    print('Відсортована матриця:')
    matrgen(ma2)
    for i in range(n):
        diag.append(ma2[i][i])
    print('Діагональ відсортованої матриці:', diag)


call()
