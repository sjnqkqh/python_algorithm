import heapq

import sys

move_arr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
INF = int(1e9)


def dijkstra(time, start_i, start_j):
    q = []
    heapq.heappush(q, (arr[start_i][start_j], start_i, start_j))
    distance[start_i][start_j] = arr[start_i][start_j]

    while q:
        dist, now_i, now_j = heapq.heappop(q)
        if dist < distance[now_i][now_j]:
            continue

        for w, i, j in graph[now_i][now_j]:
            cost = dist + w

            if cost < distance[i][j]:
                distance[i][j] = cost
                heapq.heappush(q, (cost, i, j))

    print("Problem ", time, ": ", distance[n - 1][n - 1], sep='')


input = sys.stdin.readline
time = 0
while True:
    n = int(input())
    if n == 0:
        break

    time += 1

    graph = [[[] for _ in range(n)] for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            for move in move_arr:
                next_i, next_j = i + move[0], j + move[1]
                if 0 <= next_i < n and 0 <= next_j < n:
                    graph[i][j].append((arr[next_i][next_j], next_i, next_j))

    dijkstra(time, 0, 0)
