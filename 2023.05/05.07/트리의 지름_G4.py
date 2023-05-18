import sys

sys.setrecursionlimit(1000000)

n = int(input())
dist = {}
search_start = 1


def dfs(visited: list, routes: list, idx, total_length):
    visited[idx] = True
    for node in dist[idx]:
        if not visited[node[0]]:
            routes.append((node[0], total_length + node[1]))
            dfs(visited, routes, node[0], total_length + node[1])

    return routes


for i in range(1, n + 1):
    dist[i] = []

if n == 1:
    print(0)
    quit()

for _ in range(1, n):
    s, e, v = map(int, input().split())
    dist[s].append((e, v))
    dist[e].append((s, v))

result = dfs([False] * (n + 1), [], 1, 0)
next_start = (0, 0)
for item in result:
    if item[1] > next_start[1]:
        next_start = item

result = dfs([False] * (n + 1), [], next_start[0], 0)
for item in result:
    if item[1] > next_start[1]:
        next_start = item

print(next_start[1])
