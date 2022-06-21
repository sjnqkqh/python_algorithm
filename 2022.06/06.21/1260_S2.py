# URL : https://www.acmicpc.net/problem/1260
from collections import deque


# DFS 탐색 알고리즘
def dfs(graph: list, v, visited: list):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# BFS 탐색 알고리즘
def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True  # 방문 처리

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 정점의 개수, 간선의 개수, 시작점 번호
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 간선의 갯수만큼 그래프 입력
for _ in range(m):
    temp = list(map(int, input().split()))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

# 그래프 안의 요소들 정렬 (방문할 수 있는 정점이 여러개일 경우, 정점 번호가 낮은 노드부터 방문해야 하기 때문에)
for item in graph:
    item.sort()

graph1 = graph.copy()
graph2 = graph.copy()


dfs(graph1, v, [False] * (n + 1))
print()
bfs(graph2, v, [False] * (n + 1))
