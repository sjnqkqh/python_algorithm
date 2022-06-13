# Page 149. 2트

# N, M 입력
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def dfs(x, y):
    # 그래프 범위를 초과하면 무시
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
