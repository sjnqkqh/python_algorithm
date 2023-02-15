# Page 257

INF = 1e9  # 무한

n = int(input())  # 노드의 갯수
m = int(input())  # 간선의 갯수

graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 그래프의 모든 노드 간의 거리를 무한으로 초기화

# 출발 노드와 도착 노드가 동일하다면 해당 거리는 0
for a in range(n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 따른 거리를 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INF")
        else:
            print(graph[a][b], end=" ")
    print()
