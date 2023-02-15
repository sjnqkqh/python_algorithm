# N, M 입력
from collections import deque

n, m = map(int, input().split())

# 미로 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 좌표 별 거리 배열 생성
visited = [[0] * m for _ in range(n)]


def bfs(graph, visited):
    visited[0][0] = 1  # 해당 문제에서 (1,1)은 항상 1이므로
    queue = deque([[0, 0]])
    while queue:
        v = queue.popleft()
        print(v, end=" ")

        x = v[0]
        y = v[1]

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        for i in range(4):
            distance = visited[x + dx[i]][y + dy[i]]
            if graph[x + dx[i]][y + dy[i]] == 1 and visited[x + dx[i]][y + dy[i]] == 0:
                visited[x][y] == distance + 1
                queue.append([x, y])


bfs(array, visited)
