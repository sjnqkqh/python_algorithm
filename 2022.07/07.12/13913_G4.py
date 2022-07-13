from collections import deque

N, K = map(int, input().split()) # 데이터 입력
Length = 100001 # 배열 총 길이
arr = [-1 for _ in range(Length)]

arr[N] = 0 # 탐색 시작 위치
log = {}  # 이동 경로 Dictionary
result_step = []  # 총 이동 경로 List


# BFS 탐색
def bfs(search_start):
    queue = deque()
    queue.append((search_start, 1))

    while queue:
        # Queue의 사이즈 만큼만 반복
        size = len(queue)
        for _ in range(size):
            now, cnt = queue.popleft()

            # 탐색 중 목표지 도달 시, 최소 이동 횟수 반환
            if now == K:
                return cnt

            # Node 이동 가능 범위에 따라 다음 탐색 인덱스 추가 및, Dict 에 경로 저장
            if 0 <= now + 1 < Length and arr[now + 1] == -1:
                arr[now + 1] = cnt
                queue.append((now + 1, cnt + 1))
                log[now + 1] = now

            if 0 <= now - 1 < Length and arr[now - 1] == -1:
                arr[now - 1] = cnt
                queue.append((now - 1, cnt + 1))
                log[now - 1] = now

            if 0 <= now * 2 < Length and arr[now * 2] == -1:
                arr[now * 2] = cnt
                queue.append((now * 2, cnt + 1))
                log[now * 2] = now


# BFS 탐색
result = bfs(N) - 1

# K부터 N까지 경로 Dictionary 를 탐색해, 역으로 경로 탐색
start = K
while True:
    result_step.append(start)
    if start == N:
        break
    start = log[start]

# 배열 반전
result_step.reverse()

# 답안 출력
print(result)  # 최소 이동횟수
print(*result_step, sep=" ")  # 최소 이동 경로
