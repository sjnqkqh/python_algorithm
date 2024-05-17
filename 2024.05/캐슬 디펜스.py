import copy
import itertools
import sys

from collections import deque

input = sys.stdin.readline

vector = [[0, -1], [-1, 0], [0, 1]]
result = 0
arr = []

n, m, d = map(int, input().split())
for _ in range(n):
    arr.append(list(map(int, input().split())))

combines = list(itertools.combinations(range(m), 3))


def bfs(now_i, now_j, enemy):
    queue = deque([(now_i, now_j)])
    visited = [[False] * n for _ in range(n)]
    next_queue = deque()
    cnt = 0

    while queue and cnt < d:
        now_i, now_j = queue.popleft()
        for _i, _j in vector:
            next_i = now_i + _i
            next_j = now_j + _j

            if 0 <= next_i < now_i and 0 <= next_j < m and not visited[next_i][next_j]:
                if enemy[next_i][next_j] == 1:
                    return next_i, next_j

                next_queue.append((next_i, next_j))
                visited[next_i][next_j] = True

        if len(queue) == 0:
            cnt += 1
            queue = copy.copy(next_queue)
            next_queue = deque()

    return


for comb in combines:
    comb_result = 0
    enemy = copy.deepcopy(arr)

    for time in range(n, 0, -1):
        time_results = {
            bfs(time, comb[0], enemy),
            bfs(time, comb[1], enemy),
            bfs(time, comb[2], enemy)
        }

        for time_result in time_results:
            if time_result is not None:
                i, j = time_result[0], time_result[1]
                enemy[i][j] = 0
                comb_result += 1

        result = max(result, comb_result)


print(result)
