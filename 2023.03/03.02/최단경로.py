import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
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


dijkstra(k)
for i in range(1, len(distance)):
    result = distance[i] if distance[i] != INF else 'INF'
    print(result)
