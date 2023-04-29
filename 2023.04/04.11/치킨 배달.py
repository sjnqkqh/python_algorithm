import itertools

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

c, h = [], []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            c.append([i, j])
        if arr[i][j] == 1:
            h.append([i, j])

j = list(itertools.combinations(c, M))
result = int(1e9)

for comb in j:
    x = 0
    for home in h:
        dist = int(1e9)
        for chi in comb:
            dist = min(dist,abs(home[0]-chi[0]) + abs(home[1]-chi[1]))
        x += dist
    result = min(result, x)

print(result)