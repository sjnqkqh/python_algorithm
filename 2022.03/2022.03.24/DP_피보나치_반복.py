d = [0] * 100


def fivo(x):
    d[1] = 1
    d[2] = 1

    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]

    print(d[x])


fivo(99)
