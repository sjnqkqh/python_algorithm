from collections import deque

N, M = map(int, input().split())
arr = [[0] * M] * N  # 지도
visited = [[False] * M for _ in range(N)]
move_arr = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]  # 이동 방향

for i in range(N):
    arr[i] = list(map(int, input().split()))


# BFS
def bfs(i, j):
    temp_visited = [[False] * M for _ in range(N)]
    temp_visited[i][j] = True

    queue = deque()
    queue.append([i, j])

    length = 1 # 상어까지의 거리
    while queue:
        size = len(queue)
        for _ in range(size):
            i, j = queue.popleft()

            for move in move_arr:
                next_i = i + move[0]
                next_j = j + move[1]

                if 0 <= next_i < N and 0 <= next_j < M and not temp_visited[next_i][next_j]:
                    if arr[next_i][next_j] == 0:
                        temp_visited[next_i][next_j] = True
                        queue.append([next_i, next_j])
                    else:
                        return length

        length += 1

    return length


result = -1
for i in range(N):
    for j in range(M):
        if not visited[i][j] and arr[i][j] == 0:
            visited[i][j] = True
            result = max(result, bfs(i, j))

print(result)
