from collections import deque

n, m = map(int, input().split())
queue = deque(list(map(int, input().split()))[1:])
visited = [False] * (n + 1)
party = []

for _ in range(m):
    party.append(list(map(int, input().split())))

while queue:
    p = queue.popleft()
    if not visited[p]:
        for item in party:
            if p in item[1:]:
                for t in item[1:]:
                    queue.append(t)
                visited[p] = True

for item in party:
    for x in item[1:]:
        if visited[x]:
            m -= 1
            break

print(m)
