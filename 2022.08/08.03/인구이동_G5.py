import copy
import sys
from collections import deque

N, L, R = map(int, input().split())
MOVE_ARR = [[1, 0], [0, 1], [0, -1], [-1, 0]]
visited = [[False for _ in range(N)] for _ in range(N)]

arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))


# BFS 탐색 구현
def bfs(i, j):
    total_people = arr[i][j]  # 국경이 개방되며 이주 가능한 총 인원
    country_cnt = 1  # 개방된 인접 국경의 수
    contain_point_list = [[i, j]]  # 개방된 국경의 좌표 배열

    queue = deque()
    queue.append([i, j])
    while queue:
        size = len(queue)
        for _ in range(size):
            i, j = queue.popleft()

            for move in MOVE_ARR:
                next_i = i + move[0]
                next_j = j + move[1]

                # 인접한 두 국가의 인원 차의 절대치가 L이상, R 이하인 경우엔 국경 개방
                if 0 <= next_i < N and 0 <= next_j < N and not visited[next_i][next_j] and L <= abs(arr[i][j] - arr[next_i][next_j]) <= R:
                    total_people = total_people + arr[next_i][next_j]
                    country_cnt += 1
                    contain_point_list.append([next_i, next_j])

                    queue.append([next_i, next_j])
                    visited[next_i][next_j] = True

    # 국경이 개방된 국가들과 해당 국가들의 인원 평균 반환
    return contain_point_list, int(total_people / country_cnt)


def serial_transfer():
    global visited
    global arr

    transfer_result = []
    for i in range(N):
        for j in range(N):
            # 이번 일자에 탐색하지 않은 국경이 있다면 해당 국가부터 BFS 탐색 시작
            if not visited[i][j]:
                visited[i][j] = True
                transfer_result.append(bfs(i, j))

    # 인구 이동 결과 반영
    visited = [[False for _ in range(N)] for _ in range(N)]
    for transfer in transfer_result:
        point_list = transfer[0]
        avg = transfer[1]

        # 개방된 국가들 간의 평균치로 인구 배분
        for point in point_list:
            arr[point[0]][point[1]] = avg


# 인구 이동 전후의 변화가 없다면 소요된 일자 출력
day_cnt = 0
while True:
    pre_open_arr = copy.deepcopy(arr)
    serial_transfer()

    if pre_open_arr == arr:
        print(day_cnt)
        break

    day_cnt += 1
