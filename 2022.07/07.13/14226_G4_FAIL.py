# 초기 데이터 세팅
from collections import deque

S = int(input())

arr = [-1 for _ in range(S * 2)]
arr[0], arr[1] = 0, 0

visited = [[-1 for _ in range(S * 2)] for _ in range(S * 2)]


def bfs(now, clip):
    cnt = 1
    queue = deque()
    queue.append((now, clip))
    while queue:
        size = len(queue)
        for _ in range(size):
            now, clip = queue.popleft()

            # 목표 수치에 도달했다면 반복 종료
            if now == S:
                print(cnt)
                return

            if 0 <= now - 1 < S * 2 and visited[now - 1][clip] == -1:
                visited[now - 1][clip] = cnt
                queue.append((now - 1, clip))

            if 0 <= now + clip < S * 2 and visited[now + clip][clip] == -1:
                visited[now][clip] = cnt
                queue.append((now + clip, clip))

            # 클립보드에 now를 복사
            if now > clip:
                queue.append((now, now))

        cnt += 1


bfs(1, 1)
