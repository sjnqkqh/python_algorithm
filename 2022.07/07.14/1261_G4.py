from collections import deque

M, N = map(int, input().split())
arr = [[] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)] # I, J까지 방문 체크
result_map = [[0 for _ in range(M)] for _ in range(N)] # I,J까지 이동 거리
move_arr = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 이동 방향

# 지도 입력
for i in range(N):
    arr[i] = list(map(int, input()))


# 0-1 BFS
def one_and_zero_bfs():
    visited[0][0] = True
    queue = deque()
    queue.append([0, 0, 0])

    while queue:
        i, j, cnt = queue.popleft()

        if i == N - 1 and j == M - 1:
            print(result_map[N - 1][M - 1])
            break

        for move in move_arr:
            next_i = i + move[0]
            next_j = j + move[1]

            # 0-1 BFS 탐색으로 벽이 아닌 지형을 우선적으로 탐색
            if 0 <= next_i < N and 0 <= next_j < M and not visited[next_i][next_j]:
                if arr[next_i][next_j] == 0:
                    visited[next_i][next_j] = True
                    result_map[next_i][next_j] = cnt
                    queue.appendleft([next_i, next_j, cnt])

                if arr[next_i][next_j] == 1:
                    visited[next_i][next_j] = True
                    result_map[next_i][next_j] = cnt + 1
                    queue.append([next_i, next_j, cnt + 1])


one_and_zero_bfs()
