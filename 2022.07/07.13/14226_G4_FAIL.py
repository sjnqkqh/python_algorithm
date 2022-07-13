# 초기 데이터 세팅
from collections import deque

S = int(input())

arr = [-1 for _ in range(S * 2)]
arr[0], arr[1] = 0, 0

visited = [[-1 for _ in range(S * 2)] for _ in range(S * 2)]


def bfs(now, clip):
    queue = deque()
    queue.append((now, clip))
    cnt = 1
    while queue:
        size = len(queue)
        for _ in range(size):
            now, clip = queue.popleft()

            if 0 <= now + clip < S * 2 and visited[now][clip] == -1:
                visited[now][clip] = cnt
                queue.append((now + clip, clip))

            if 0 <= now - 1 < S * 2 and visited[now - 1][clip] == -1:
                visited[now - 1][clip] = cnt
                queue.append((now - 1, clip))

            # 클립보드에 now를 복사
            if now > clip:
                queue.append((now, now))

        cnt += 1


bfs(1, 1)
Min = int(1e9)
for item in visited[S]:
    if item != -1:
        Min = min(item, Min)
print(Min)
