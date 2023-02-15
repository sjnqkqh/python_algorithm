from collections import deque

M, N = map(int, input().split())
arr = [[] * M] * N
for i in range(N):
    arr[i] = list(input())

move_arr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visited = [[False for _ in range(M)] for _ in range(N)]

white_team = []  # 아군 덩어리 배열
blue_team = []  # 적군 덩어리 배열


def dfs(i, j):
    color = ""  # 탐색할 색
    queue = deque()
    queue.append([i, j])
    person_cnt = 0

    while queue:
        i, j = queue.popleft()
        color = arr[i][j]
        person_cnt += 1

        for move in move_arr:
            next_i = i + move[0]
            next_j = j + move[1]

            if (
                0 <= next_i < N
                and 0 <= next_j < M
                and not visited[next_i][next_j]
                and arr[next_i][next_j] == color
            ):
                visited[next_i][next_j] = True
                queue.append([next_i, next_j])

    # 탐색 종료 이후 탐색한 색상에 따라 적/아군 수 대입
    return color, person_cnt


keepSearch = True
while keepSearch:
    keepSearch = False
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                visited[i][j] = True
                color, person_cnt = dfs(i, j)
                keepSearch = True
                if color == "W":
                    white_team.append(person_cnt)
                else:
                    blue_team.append(person_cnt)

# 최종 전투력 합산
sameTeamCnt = 0
enemyTeamCnt = 0

for item in white_team:
    sameTeamCnt += item**2

for item in blue_team:
    enemyTeamCnt += item**2

print(sameTeamCnt, enemyTeamCnt)
