import heapq
import sys

input = sys.stdin.readline

bus = set()
n = int(input()) + 1
m = int(input())

INF = int(1e9)
arr = [[INF] * n for _ in range(n)]
for i in range(n):
    arr[i][i] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    bus.add((cost, a, b))

while bus:
    c, a, b = bus.pop()

    if arr[a][b] > c:
        arr[a][b] = c

for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            if arr[j][i] + arr[i][k] < arr[j][k]:
                arr[j][k] = arr[j][i] + arr[i][k]

for i in range(1, n):
    for j in range(1, n):
        print(arr[i][j] if arr[i][j] != INF else 0, end=" ")
    print()
