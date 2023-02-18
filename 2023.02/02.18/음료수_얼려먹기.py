def dfs(i, j):
    for move in vector:
        next_i, next_j = i + move[0], j + move[1]
        if n > next_j >= 0 and m > next_i >= 0 and graph[next_j][next_i] == 0 and not visited[next_j][next_i]:
            visited[next_j][next_i] = True
            dfs(next_j, next_i)


vector = [[1, 0], [0, 1], [-1, 0], [0, -1]]
result = 0

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            result += 1
            dfs(i, j)

print(result)
