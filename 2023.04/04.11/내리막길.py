move_arr = [[1, 0], [0, 1], [-1, 0], [0, -1]]
arr = []
visited = []
result = 0


def dfs(i, j):
    global result
    if i == n - 1 and j == m - 1:
        result += 1
        return

    for move in move_arr:
        ni, nj = i + move[0], j + move[1]

        if n > ni >= 0 and m > nj >= 0 and not visited[ni][nj] and arr[i][j] > arr[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj)
            visited[ni][nj] = False


n, m = map(int, input().split())
for _ in range(n):
    arr.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

dfs(0, 0)
print(result)
