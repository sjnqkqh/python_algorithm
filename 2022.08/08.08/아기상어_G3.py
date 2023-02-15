from collections import deque

N = int(input())
arr = []
move_arr = [[-1, 0], [0, -1], [1, 0], [0, 1]]
start_i, start_j = 0, 0

# 지도 입력
for i in range(N):
    arr.append(list(map(int, input().split())))

# 탐색 시작 위치 설정
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            start_i, start_j = i, j

turning_cnt = 0  # 섭식 횟수
shark_scale = 2  # 상어의 초기 크기
result = 0  # 결과


# BFS 탐색
def bfs(scale, start_i, start_j, visited: list):
    global arr
    queue = deque()
    queue.append([start_i, start_j])
    visited[start_i][start_j] = True
    move_cnt = 0

    while queue:
        size = len(queue)

        # 이 시점에서 큐에 있는 데이터들을 모두 확인하며, 잡아먹을 수 있는 좌표 중, Y좌표가 가장 크고, X좌표가 가장 작은 노드를 반환해야 함
        result_i, result_j, finish_this_time = int(1e9), int(1e9), False
        for item in queue:
            if (
                arr[item[0]][item[1]] != 0
                and arr[item[0]][item[1]] != 9
                and scale > arr[item[0]][item[1]]
            ):
                finish_this_time = True
                if result_i > item[0]:
                    result_i, result_j = item[0], item[1]

                if result_i == item[0] and result_j > item[1]:
                    result_j = item[1]

        # 선별된 노드 0으로 초기화 후, 결과값 반환
        if finish_this_time:
            arr[result_i][result_j] = 0
            return move_cnt, result_i, result_j

        for _ in range(size):
            i, j = queue.popleft()

            for move in move_arr:
                next_i = i + move[0]
                next_j = j + move[1]

                if (
                    0 <= next_i < N
                    and 0 <= next_j < N
                    and not visited[next_i][next_j]
                    and (
                        arr[next_i][next_j] == 0
                        or arr[next_i][next_j] == 9
                        or scale >= arr[next_i][next_j]
                    )
                ):
                    queue.append([next_i, next_j])
                    visited[next_i][next_j] = True

        move_cnt += 1

    # 더 이상 먹을 수 있는 물고기가 없으면 0 반환 및 탐색 종료
    return 0, None, None


while True:
    search_result, finish_i, finish_j = bfs(
        shark_scale, start_i, start_j, [[False for _ in range(N)] for _ in range(N)]
    )

    # 먹을 수 있는 물고기가 없으면 반복 종료
    if search_result == 0:
        print(result)
        break
    else:
        # 섭식 이후앤, 해당 노드에서부터 다시 시작
        result += search_result
        start_i = finish_i
        start_j = finish_j
        turning_cnt += 1

    # 상어의 크기만큼 물고기를 섭식했다면, 크기 증가
    if turning_cnt == shark_scale:
        shark_scale += 1
        turning_cnt = 0
