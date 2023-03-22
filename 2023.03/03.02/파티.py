import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [set() for _ in range(n + 1)]

for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].add((v,w))

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
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

result = -1
for i in range(1,n+1):
    result = max(result, dijkstra(i)[x]+dijkstra(x)[i])

print(result)
