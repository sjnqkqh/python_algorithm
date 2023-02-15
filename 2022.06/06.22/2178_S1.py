# URL : https://www.acmicpc.net/problem/2178
from collections import deque


def bfs(graph, x, y, visited):
    move_arr = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        v = queue.popleft()
        for move in move_arr:
            x = v[0] + move[0]
            y = v[1] + move[1]

            if 0 <= x < n and 0 <= y < m:
                if graph[x][y] != 0 and not visited[x][y]:
                    queue.append([x, y])
                    visited[x][y] = True
                    graph[x][y] = graph[v[0]][v[1]] + 1


n, m = map(int, input().split())
graph = []
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input())))

bfs(graph, 0, 0, visited)

print(graph[n - 1][m - 1])
