import heapq

n, m, c = map(int, input().split(' '))
INF = int(1e9)
distance_arr = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    distance_arr[i][i] = 0

for i in range(m):
    start, end, distance = map(int, input().split(' '))
    distance_arr[start][end] = distance


def dijkstra(start):
    queue = []

    for i in range(1, n + 1):
        if i != start and distance_arr[start][i] != INF:
            heapq.heappush(queue, (distance_arr[start][i], i))

    while queue:
        distance, point = heapq.heappop(queue)

        for i in range(1, n + 1):
            if distance_arr[start][i] > distance_arr[start][point] + distance_arr[point][i]:
                distance_arr[start][i] = distance_arr[start][point] + distance_arr[point][i]
                heapq.heappush(queue, (distance_arr[point][i], i))


dijkstra(c)
city_count, max_time = 0, 0

for item in distance_arr[c]:

    if item != 0 and item != INF:
        max_time = max(max_time,item)
        city_count += 1

print(city_count, max_time)