from collections import deque

M, N = map(int, input().split())
arr = [[] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
move_arr = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 이동 방향
# 지도 입력
for i in range(N):
    arr[i] = list(map(int, input()))


# 0-1 BFS
def one_and_zero_bfs():
    visited[0][0] = True
    result = 0
    queue = deque()
    queue.append([0, 0])

    while queue:
        i, j = queue.popleft()

        # 벽을 부시게 되면 결과값 1 증가
        if arr[i][j] == 1:
            print(i, j)
            result += 1

        if i == N - 1 and j == M - 1:
            print(result)
            break

        for move in move_arr:
            next_i = i + move[0]
            next_j = j + move[1]

            # 0-1 BFS 탐색으로 벽이 아닌 지형을 우선적으로 탐색
            if 0 <= next_i < N and 0 <= next_j < M and not visited[next_i][next_j]:
                if arr[next_i][next_j] == 0:
                    visited[next_i][next_j] = True
                    queue.appendleft([next_i, next_j])
                    break

                else:
                    visited[next_i][next_j] = True
                    queue.append([next_i, next_j])
                    break


one_and_zero_bfs()
