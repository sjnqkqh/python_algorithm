# URL : https://www.acmicpc.net/problem/10845

from collections import deque

n = int(input())
queue = deque()
arr = []
for _ in range(n):
    arr.append(list(input().split()))

for order in arr:
    action = order[0]
    if action == "push":
        queue.append(int(order[1]))
    elif action == "pop":
        print(-1 if len(queue) == 0 else queue.popleft())
    elif action == "size":
        print(len(queue))
    elif action == "empty":
        print(1 if len(queue) == 0 else 0)
    elif action == "front":
        print(-1 if len(queue) == 0 else queue[0])
    elif action == "back":
        print(-1 if len(queue) == 0 else queue[len(queue) - 1])
