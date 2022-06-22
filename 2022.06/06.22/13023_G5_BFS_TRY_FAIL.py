# URL : https://www.acmicpc.net/problem/13023
from collections import deque


# BFS 탐색
def bfs(graph, start):
    link_count = 0
    passed = [start]
    queue = deque()
    queue.append(graph[start])

    while queue:
        v = queue.popleft()
        for i in v:
            if i not in passed:
                queue.append(graph[i])
                passed.append(i)
                link_count += 1
                break

    if link_count == 5:
        return 1
    else:
        return 0


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(graph, 0))

# 2 7 4 3 5
