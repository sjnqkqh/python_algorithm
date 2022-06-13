# Page 151
# 일단 BFS가 아닌 DFS로 해결해야하는 문제였음

# n, m 입력
n, m = map(int, input().split())
result = 0;

# 2차원 그래프 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


# DFS로 특정 노드 방문 이후 인접한 다른 노드들도 방문
def dfs(x, y):
    # 가능 범위를 넘어서면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문한 적 없다면
    if graph[x][y] == 0:
        graph[x][y] = 1  # 해당 노드 방문처리
        # 해당 노드의 상하좌우 노드도 방문처리
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


# 모든 노드에 대해서 방문 처리
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
