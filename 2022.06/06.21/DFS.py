def dfs(graph: list, v: int, visited: list):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=" ")

    # 현재 그래프에서 방문하지 않은 노드 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * 9

dfs(graph, 1, visited=visited)
