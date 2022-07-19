from collections import deque

S, T = map(int, input().split())

# 범위 내의 모든 2의 제곱수 목록 반환
i = 1
square_nums = []
while i <= int(1e9):
    square_nums.append(i)
    i = i * 2


# 시작수와 목표수가 도달 가능한 관계인지 반환
def is_possible(start, target):
    # target이 2의 제곱수라면 True
    if target in square_nums:
        return True

    # 시작수가 목표수의 약수라면 True
    if target % start == 0:
        return True

    # 그 외의 경우엔 도달 할 수 없음
    return False


# 시작수와 목표수가 같거나 도달할 수 없다면 즉시 종료
def default_number_check():
    if S == T:
        return "0"

    if not is_possible(S, T):
        return "-1"

    if T == 1:
        return "/"

    return True


# +, * 기준 BFS 탐색
def bfs():
    step = ""
    visited = set()

    queue = deque()
    queue.append((1, "/"))
    queue.append((S, step))

    while queue:
        now, step = queue.popleft()
        if now == T:
            return step

        if now not in visited:
            visited.add(now)
            if now * now <= T:
                queue.append((now * now, step + "*"))

            if now * 2 <= T:
                queue.append((now * 2, step + "+"))

    return -1


check_result = default_number_check()
if not check_result == True:
    print(check_result)
else:
    result = bfs()
    print(result)
