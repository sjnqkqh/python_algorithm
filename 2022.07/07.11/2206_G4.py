# 지도 크기 입력
from collections import deque

N, M = map(int, input().split())
arr = []
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

# 상하좌우 이동 배열
move_arr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 지도 입력
for _ in range(N):
    arr.append(list(map(int, input())))


# # BFS
def bfs():
    queue = deque()
    queue.append([0, 0, 0])
    visited[0][0][0] = 1  # 벽을 한 번도 뚫지 않은 상태에서 시작점 방문 처리

    while queue:
        size = len(queue)
        for _ in range(size):
            i, j, wall = queue.popleft()

            if i == N - 1 and j == M - 1:
                return visited[i][j][wall]

            for move in move_arr:
                next_i = i + move[0]
                next_j = j + move[1]
                if 0 <= next_i < N and 0 <= next_j < M:
                    if arr[next_i][next_j] == 0 and visited[next_i][next_j][wall] == 0:
                        visited[next_i][next_j][wall] = visited[i][j][wall] + 1
                        queue.append([next_i, next_j, wall])

                    if arr[next_i][next_j] == 1 and wall == 0:  # 벽을 한 번도 부수지 않은 상태로, 벽을 마주했다면
                        visited[next_i][next_j][1] = visited[i][j][wall] + 1
                        queue.append([next_i, next_j, 1])

    return -1


print(bfs())
