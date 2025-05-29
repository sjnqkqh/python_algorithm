import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) + 1
lines = int(input())
arr = [[False for _ in range(n)] for _ in range(n)]

for _ in range(lines):
    i, j = map(int, input().split())
    arr[i][j], arr[j][i] = True, True




visited = [False] * n
queue = deque([1])
visited[1] = True

while queue:
    now = queue.pop()
    visited[now] = True

    for i in range(n):
        next = arr[now][i]
        if next and not visited[i]:
            queue.append(i)

print(visited.count(True) - 1)
