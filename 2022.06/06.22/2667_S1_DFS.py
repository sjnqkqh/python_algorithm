# URL : https://www.acmicpc.net/problem/2667

# DFS 탐색
def dfs(graph: list, x: int, y: int, visited: list):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 0:
        return False

    if not visited[x][y]:
        visited[x][y] = True
        dfs(graph, x - 1, y, visited)
        dfs(graph, x, y - 1, visited)
        dfs(graph, x + 1, y, visited)
        dfs(graph, x, y + 1, visited)
        return True
    return False


# graph[x][y]가 속한 단지의 집의 수 탐색
def get_house_count(graph, x, y, visited, cnt):
    if x < 0 or x >= n or y < 0 or y >= n:
        return cnt

    if graph[x][y] == 0:
        return cnt

    if not visited[x][y]:
        visited[x][y] = True
        cnt = cnt + 1
        cnt = get_house_count(graph, x - 1, y, visited, cnt)
        cnt = get_house_count(graph, x, y - 1, visited, cnt)
        cnt = get_house_count(graph, x + 1, y, visited, cnt)
        cnt = get_house_count(graph, x, y + 1, visited, cnt)
        return cnt
    return cnt


n = int(input())
graph = []
result = 0
resultArray = []
visited = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if dfs(graph, i, j, visited):
            # DFS 결과가 참인 경우 (한 개의 단지에 대해 탐색이 끝났을 때), graph[i][j]가 속한 단지의 갯수를 탐색
            resultArray.append(get_house_count(graph, i, j, visited2, 0))
            result = result + 1

# 정답 출력
resultArray.sort()
print(result)
for item in resultArray:
    print(item)