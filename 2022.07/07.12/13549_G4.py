from collections import deque

N, K = map(int, input().split())
length = 100001

queue = deque()
queue.append(N)

visited = [-1 for _ in range(length)]
visited[N] = 0
result = []

while queue:
    s = queue.popleft()  # 현재 위치
    result.append(s)

    if s == K:  # 누나가 동생을 따라잡으면 중단
        print(visited[s])
        print(result)
        break

    if 0 <= s * 2 < length and visited[s * 2] == -1:
        visited[s * 2] = visited[s]
        queue.appendleft(s * 2)

    if 0 <= s - 1 < length and visited[s - 1] == -1:
        visited[s - 1] = visited[s] + 1
        queue.append(s - 1)

    if 0 <= s + 1 < length and visited[s + 1] == -1:
        visited[s + 1] = visited[s] + 1
        queue.append(s + 1)
