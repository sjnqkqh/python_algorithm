import copy
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [set() for _ in range(n + 1)]
distance = [INF] * (n + 1)
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].add((b, c))
    graph[b].add((a, c))

u, v = map(int, input().split())


def dijkstra(graph, distance, start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist < distance[now]:
            continue

        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

    return distance


result_1 = dijkstra(copy.deepcopy(graph), copy.deepcopy(distance), 1)
result_u = dijkstra(copy.deepcopy(graph), copy.deepcopy(distance), u)
result_v = dijkstra(copy.deepcopy(graph), copy.deepcopy(distance), v)

result = min(
    result_1[u] + result_u[v] + result_v[n],
    result_1[v] + result_v[u] + result_u[n]
)

if result >= INF:
    print(-1)
else:
    print(result)
