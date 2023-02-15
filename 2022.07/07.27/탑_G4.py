from collections import deque

N = int(input())
queue = deque(list(map(int, input().split())))
stack = []
result = []

index = 0
while queue:
    now = queue.popleft()
    index += 1

    while stack:
        if stack[-1][1] > now:
            # 송신 타워가 존재하는 경우 -> 기존 타워는 그대로 두고 그 위에 now를 얹음
            result.append(stack[-1][0])
            stack.append((index, now))
            break
        else:
            # 스택의 맨 윗칸이 now보다 작으면 더 큰 게 나올때까지 치워버림
            stack.pop()

    if len(stack) == 0:
        result.append(0)
        stack.append((index, now))

print(*result, sep=" ")
