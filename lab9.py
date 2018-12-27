def strings():
    line = str(input('Enter some text with SPACE:'))
    spl = line.split()
    print(line)
    x = spl.index(max(spl, key=len))
    y = spl.index(min(spl, key=len))
    print(x, y)
    spl[x], spl[y] = spl[y], spl[x]
    print('|'.join(spl))


strings()
