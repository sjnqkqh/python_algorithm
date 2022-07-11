# 지도 크기 입력
from collections import deque

N, M = map(int, input().split())
arr = []
visited = [[[False, False] for _ in range(M)] for _ in range(N)]
graph = [[[int(1e9), int(1e9)] for _ in range(M)] for _ in range(N)]

# 상하좌우 이동 배열
move_arr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 지도 입력
for _ in range(N):
    arr.append(list(map(int, input())))


# # BFS
def bfs():
    queue = deque()
    queue.append([0, 0, True])
    visited[0][0][0] = True  # 벽을 한 번도 뚫지 않은 상태에서 시작점 방문 처리
    graph[0][0][0] = 1
    graph[0][0][1] = 1

    while queue:
        size = len(queue)
        for _ in range(size):
            i, j, not_crashed_yet = queue.popleft()

            for move in move_arr:
                next_i = i + move[0]
                next_j = j + move[1]

                if 0 <= next_i < N and 0 <= next_j < M:
                    if arr[next_i][next_j] == 0:
                        if not visited[next_i][next_j][0]:
                            graph[next_i][next_j][0] = graph[i][j][0] + 1
                            visited[next_i][next_j][0] = True
                            queue.append([next_i, next_j, not_crashed_yet])

                        if not visited[next_i][next_j][1]:
                            graph[next_i][next_j][1] = graph[i][j][1] + 1
                            visited[next_i][next_j][1] = True
                            queue.append([next_i, next_j, False])

                    else:
                        if not visited[next_i][next_j][1] and not_crashed_yet:
                            graph[next_i][next_j][1] = graph[i][j][1] + 1
                            visited[next_i][next_j][1] = True
                            queue.append([next_i, next_j, False])

    result = min(graph[N - 1][M - 1][0], graph[N - 1][M - 1][1]) if visited[N - 1][M - 1][0] or visited[N - 1][M - 1][1] else -1
    print(result)


bfs()
