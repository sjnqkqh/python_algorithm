from collections import deque


def bfs():
    queue = deque([])
    queue.append([0, 0])

    while queue:
        i, j = queue.popleft()
        visited[i][j] = True
        if i == n - 1 and j == m - 1:
            return

        for move in move_arr:
            next_i, next_j = i + move[0], j + move[1]
            if n > next_i >= 0 and m > next_j >= 0 and not visited[next_i][next_j] and graph[next_i][next_j] != 0:
                queue.append([next_i, next_j])
                graph[next_i][next_j] = graph[i][j] + 1


move_arr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
n, m = map(int, input().split(' '))
visited = [[False] * m for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

bfs()

for _ in graph:
    print(_)
