n, m, r = map(int, input().split())
item_count = list(map(int, input().split()))
INF = 10 ** 8
arr = [[INF] * n for _ in range(n)]

for i in range(n):
    arr[i][i] = 0

for _ in range(r):
    a, b, length = map(int, input().split())
    arr[a - 1][b - 1] = length
    arr[b - 1][a - 1] = length

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

result = -1
for i in range(n):
    point_sum = 0
    for j in range(n):
        if arr[i][j] <= m:
            point_sum += item_count[j]

    result = max(result, point_sum)

print(result)
