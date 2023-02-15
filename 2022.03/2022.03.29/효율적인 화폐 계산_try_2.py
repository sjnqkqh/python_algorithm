# Page 228

n, m = map(int, input().split())

INF = 10001
d = [INF for i in range(m + 1)]
bills = []

for i in range(n):
    bills.append(int(input()))

d[0] = 0

for i in range(1, m + 1):
    for bill in bills:
        if i % bill == 0:
            d[i] = min(d[i], (d[i - bill] + 1))

if d[m] == INF:
    print(-1)
else:
    print(d[m])
