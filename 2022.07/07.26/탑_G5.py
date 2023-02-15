from collections import deque

N = int(input())
stack = list(map(int, input().split()))
result = deque()  # 정답 저장용 데크

# 탐색 시작
while stack:
    tower = stack.pop()
    receive_able = False
    pass_cnt = 1
    # 발신 타워보다 앞선 타워들의 높이를 탐색하며, 더 높은 타워 탐색
    while stack:
        next_tower = stack.pop()
        if next_tower > tower:
            receive_able = True
            break
        else:
            pass_cnt = pass_cnt + 1

    # 수신이 가능한 타워가 없다면, 데크에 0 삽입
    for _ in range(N - pass_cnt):
        if receive_able:
            result.appendleft(N - pass_cnt)
        else:
            result.appendleft(0)

for item in result:
    print(item, end=" ")
