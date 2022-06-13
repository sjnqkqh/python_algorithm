# N, M 입력
from collections import deque

n, m = map(int, input().split())

# 미로 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 이동 방향 생성
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 소스코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4방향으로 반복
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 이탈한 경우 무효 처리
            if nx < 0 or ny < 0 or n <= nx or m <= ny:
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우 거리 계산
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))
