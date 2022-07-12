import sys
from collections import deque
from pprint import pprint

sys.setrecursionlimit(int(1e9))

N, K = map(int, input().split())
INF = int(1e9)
Length = 100001
arr = [-1 for _ in range(Length)]

arr[N] = 0


# BFS
def bfs(start):
    queue = deque()
    queue.append((start, 1))

    while queue:
        size = len(queue)
        for _ in range(size):
            now, cnt = queue.popleft()

            if now == K:
                return cnt

            if 0 <= now + 1 < Length and arr[now + 1] == -1:
                arr[now + 1] = cnt
                queue.append((now + 1, cnt + 1))

            if 0 <= now - 1 < Length and arr[now - 1] == -1:
                arr[now - 1] = cnt
                queue.append((now - 1, cnt + 1))

            if 0 <= now * 2 < Length and arr[now * 2] == -1:
                arr[now * 2] = cnt
                queue.append((now * 2, cnt + 1))


# def tracking_dfs(start, depth, visited, log: list):
#     visited[start] = True
#     log.append(start)
#
#     # 트랙킹 종료 시, 리스트 반전하여 출력
#     if depth == 1:
#         log.reverse()
#         print(*log, sep=" ")
#         return
#
#     if 0 <= start - 1 < Length and depth - 2 == arr[start - 1] and not visited[start-1]:
#         tracking_dfs(start - 1, depth - 1, visited, log)
#         return
#
#     if start % 2 == 0 and depth - 2 == arr[start // 2] and not visited[start-1]:
#         tracking_dfs(start // 2, depth - 1, visited, log)
#         return
#
#     if 0 <= start + 1 < Length and depth - 2 == arr[start + 1] and not visited[start-1]:
#         tracking_dfs(start + 1, depth - 1, visited, log)
#         return

def tracking_bfs():
    visited = [False for _ in range(Length)]

    queue = deque()
    queue.append((1, N, []))

    while queue:
        step, point, log = queue.popleft()
        log: list

        if step == depth:
            print(log)

        if 0 <= point * 2 < Length and arr[point * 2] == step and not visited[point * 2]:
            visited[point * 2] = True
            queue.append((step + 1, point * 2, log.append(point * 2)))

        if 0 <= point - 1 < Length and arr[point - 1] == step and not visited[point - 1]:
            visited[point - 1] = True
            queue.append((step + 1, point * 2, log.append(point - 1)))

        if 0 <= point + 1 < Length and arr[point + 1] == step and not visited[point + 1]:
            visited[point + 1] = True
            queue.append((step + 1, point * 2, log.append(point + 1)))

        step += 1


depth = bfs(N)

print(depth - 1)  # 최소 이동횟수
tracking_bfs()  # 최소 이동 경로
