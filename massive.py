import random

z = int(input("Введіть число від 1 до 20:"))
rlist = []
for i in range(0, 20):
    x = random.randint(0, 20)
    rlist.append(x)
print(rlist)
k = 0
listz = []
for i in range(0, 20):
    if rlist[k] < z:
        listz.append(rlist[k])
    k += 1
print("Масив елементів < z =", listz)
print('Його довжина:', len(listz))
x = max(listz)
print('Його максимальний елемент:', x)
l = int(len(listz))
n = 0
for i in range(0, l):
    if listz[i] == x:
        print('Його індекс:', listz.index(x))
        rlist[n], listz[i] = listz[i], rlist[n]
        h = int(listz[i])
        n = int(listz[n])
        break
for i in range(n, l):
    if listz[i] == x:
        listz[i] = h
print('Фінальний массив виконаний зі всіма умовами =', listz)
input('press ENTER to exit')
