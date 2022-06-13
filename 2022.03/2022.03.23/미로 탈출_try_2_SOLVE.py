# Page 152. 2트

from collections import deque

# N, M 입력
n, m = map(int, input().split())

# 그래프 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 이동 방향 설정
dx = [0, 0, - 1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] != 1:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    print(graph)
    return graph[n - 1][m - 1]


print(bfs(0, 0))
