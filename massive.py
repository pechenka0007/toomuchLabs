import random

z = int(input("Введіть число від 1 до 20:"))


def massgen():
    rlist = []
    for i in range(0, 20):
        rlist.append(random.randint(0, 20))
    return rlist


def masssort(rlist):
    print('Массив:', rlist)
    listz = []
    for i in range(0, 20):
        if rlist[i] < z:
            listz.append(rlist[i])
    print("Масив елементів < z =", listz)
    print('Його довжина:', len(listz))
    x = max(listz)
    print('Його максимальний елемент:', x)
    return x, listz


def massrepl(x, listz, rlist):
    n = 0
    h = 0
    l = int(len(listz))
    for i in range(0, l):
        if listz[i] == x:
            print('Його індекс:', listz.index(x))
            rlist[0], listz[i] = listz[i], rlist[0]
            h = int(listz[i])
            n = int(listz[0])
            break
    return n, h, l


def massfinal(n, h, x, listz, rlist):
    for i in range(n, l):
        if listz[i] == x:
            listz[i] = h
    print('Фінальний массив виконаний зі всіма умовами =', listz)
    print('Початковий масив, зі зміненим елементом:', rlist)
    input('press ENTER to exit')


rlist = massgen()
x, listz = masssort(rlist)
n, h, l = massrepl(x, listz, rlist)
massfinal(n, h, x, listz, rlist)

