import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
arr = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (n + 1)


def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = True

    while queue:
        i = queue.popleft()

        for item in arr[i]:
            if not visited[item]:
                visited[item] = True
                queue.append(item)


bfs()
print(visited.count(True)-1)
