import sys

input = sys.stdin.readline


def dfs(index, routes: list, length):
    visited[index] = True
    for link in dist[index]:
        if not visited[link[0]]:
            routes.append((link[0], length + link[1]))
            dfs(link[0], routes, length + link[1])

    return routes


n = int(input()) + 1
visited = [False] * n
dist = {}

for _ in range(1, n):
    line = list(map(int, input().split()))
    start, m = line[0], line[1:-1]
    for i in range(0, len(m), 2):
        if dist.get(start) is None:
            dist[start] = [(m[i], m[i + 1])]
        else:
            dist[start].append((m[i], m[i + 1]))

longest = (1, 0)
for _ in range(2):
    result = dfs(longest[0], [], 0)
    visited = [False] * n
    for i in range(len(result)):
        route = result[i]
        if longest[1] < route[1]:
            longest = route

print(longest[1])
