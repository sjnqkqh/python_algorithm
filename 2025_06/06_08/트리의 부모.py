import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n + 1)]
visited = [False] * len(arr)

for _ in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

queue = deque()
queue.append((1, arr[1]))
visited[1] = True
parent_arr = [i for i in range(len(arr))]

while queue:
    parent_index, child_arr = queue.popleft()
    for child in child_arr:
        if not visited[child]:
            parent_arr[child] = parent_index
            queue.append((child, arr[child]))
            visited[child] = True

for i in range(2, len(parent_arr)):
    print(parent_arr[i])
