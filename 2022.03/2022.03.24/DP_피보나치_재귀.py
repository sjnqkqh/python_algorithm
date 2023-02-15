# Page 214

d = [0] * 100


def fivo(x):
    print("f(" + str(x) + ")", end=" ")
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fivo(x - 1) + fivo(x - 2)
    return d[x]


print(fivo(99))
