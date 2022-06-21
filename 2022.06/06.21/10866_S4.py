# URL : https://www.acmicpc.net/problem/10866

from collections import deque

n = int(input())
queue = deque()
arr = []
for _ in range(n):
    arr.append(list(input().split()))

for order in arr:
    action = order[0]
    if action == 'push_front':
        queue.appendleft(int(order[1]))
    elif action == 'push_back':
        queue.append(int(order[1]))
    elif action == 'pop_front':
        print(-1 if len(queue) == 0 else queue.popleft())
    elif action == 'pop_back':
        print(-1 if len(queue) == 0 else queue.pop())
    elif action == 'size':
        print(len(queue))
    elif action == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif action == 'front':
        print(-1 if len(queue) == 0 else queue[0])
    elif action == 'back':
        print(-1 if len(queue) == 0 else queue[len(queue) - 1])
