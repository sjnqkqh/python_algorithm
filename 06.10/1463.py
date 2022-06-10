# URL : https://www.acmicpc.net/problem/1463

n = int(input())

d = [0 for i in range(n + 1)]
divList = [3, 2]

if n >= 2:
    d[2] = 1
if n >= 3:
    d[3] = 1

for i in range(3, n + 1):
    d[i] = d[i - 1] + 1
    for div in divList:
        if i % div == 0:
            d[i] = min(d[i], d[i // div] + 1)

print(d[n])
