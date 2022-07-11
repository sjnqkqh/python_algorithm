import math
from collections import deque

n, m = map(int, input().split())
ladders = []
snakes = []
visited = [False for _ in range(101)]
graph = [int(1e9) for _ in range(101)]

# 사다리 입력
for i in range(n):
    ladders.append(list(map(int, input().split())))

# 뱀 입력
for i in range(m):
    snakes.append(list(map(int, input().split())))


# BFS
def bfs(point, visited: list):
    result = 1
    queue = deque()
    visited[0] = True
    visited[1] = True
    queue.append(point)

    while queue:
        size = len(queue)
        for i in range(size):
            point = queue.popleft()

            if point == 100:
                print(graph[100])
                return

            for j in range(1, 7):
                if 0 <= point + j < 101 and not visited[point + j]:
                    next_idx = point+j

                    for snake in snakes:
                        if next_idx == snake[0]:
                            next_idx = snake[1]

                    for ladder in ladders:
                        if next_idx == ladder[0]:
                            next_idx = ladder[1]

                    visited[next_idx] = True
                    graph[next_idx] = min(result, graph[point] + 1)
                    queue.append(next_idx)

        result += 1


bfs(1, visited)
