# 인접 행렬 표현식
INF = 9999999999

graph = [[0, 7, 5], [7, 0, INF], [5, INF, 0]]

print(graph)

# 인접 리스트 표현식
graph = [[] for _ in range(3)]
graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)
