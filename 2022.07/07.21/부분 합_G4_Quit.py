from collections import deque

N, S = map(int, input().split())
arr = list(map(int, input().split()))
min_length = int(1e9)
queue = deque()
sum = 0

for i in range(len(arr)+1):
    while sum >= S:
        min_length = min(min_length, len(queue))
        sum -= queue.popleft()

    if i < len(arr):
        queue.append(arr[i])
        sum += arr[i]

print(min_length if min_length != int(1e9) else 0)
