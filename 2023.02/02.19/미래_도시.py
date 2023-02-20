import heapq

INF = int(1e9)

n, m = map(int, input().split(' '))
route_array = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    route_array[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split(' '))
    route_array[a][b], route_array[b][a] = 1, 1

x, k = map(int, input().split())


def distance_calculate():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                route_array[i][j] = min(route_array[i][j], route_array[i][k] + route_array[k][j])


distance_calculate()
dist_1 = route_array[1][k]
dist_2 = route_array[k][x]

if dist_1 == INF or dist_2 == INF:
    print(-1)
else:
    print(dist_1+dist_2)