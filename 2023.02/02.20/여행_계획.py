import heapq


# 다익스트라 알고리즘 사용하여 이동 가능한지 확인
def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 0))

    while queue:
        dist, city = heapq.heappop(queue)
        visited[city] = True
        connect = graph[city]

        for i in range(m):
            if connect[i] == 1:
                graph[city][i] = 1

                if distance[i] == INF:
                    distance[i] = 1

                if not visited[i]:
                    heapq.heappush(queue, (1, i))


n, m = map(int, input().split())
INF = int(1e9)
result = "YES"

distance = [INF] * n
visited = [False] * n
graph = []

for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
target_arr = list(map(int, input().split()))

dijkstra()

for city in target_arr:
    if not visited[city-1]:
        result = "NO"

print(result)
