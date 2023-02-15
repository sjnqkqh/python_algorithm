from collections import deque

N, K = map(int, input().split())
length = max(N, K) * 2
arr = [[-1 for _ in range(3)] for _ in range(length)]


def bfs():
    queue = deque()
    queue.append(N)
    arr[N][0], arr[N][1], arr[N][2] = 0, 0, 0
    step = 1
    while queue:
        size = len(queue)
        for _ in range(size):
            now = queue.popleft()
            if now * 2 < length and arr[now * 2][0] == -1:
                arr[now * 2][0] = step
                queue.append(now * 2)
            if 0 <= now - 1 < length and arr[now - 1][1] == -1:
                arr[now - 1][1] = step
                queue.append(now - 1)
            if 0 <= now + 1 < length and arr[now + 1][2] == -1:
                arr[now + 1][2] = step
                queue.append(now + 1)

        step += 1


bfs()
result = 1e9
for item in arr[K]:
    if item != -1:
        result = min(result, item)

print(result)
result2 = 0
if K % 2 == 0:
    result2 += arr[K // 2].count(result - 1)

result2 += arr[K - 1].count(result - 1)
result2 += arr[K + 1].count(result - 1)

print(result2)
