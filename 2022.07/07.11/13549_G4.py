from collections import deque

n, k = map(int, input().split())
arrayLength = 100001

queue = deque()
queue.append(n)

visited = [-1 for _ in range(arrayLength)]
visited[n] = 0

while queue:
    s = queue.popleft()
    if s == k:
        print(visited[s])
        break

    if 0 <= s - 1 < arrayLength and visited[s - 1] == -1:
        visited[s - 1] = visited[s] + 1
        queue.append(s - 1)

    if 0 <= s * 2 < arrayLength and visited[s * 2] == -1:
        visited[s * 2] = visited[s]
        queue.appendleft(s * 2)

    if 0 <= s + 1 < arrayLength and visited[s + 1] == -1:
        visited[s + 1] = visited[s] + 1
        queue.append(s + 1)
