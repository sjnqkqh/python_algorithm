from collections import deque


def special_calc(num: int):
    if (num - 1) % 10 != 0:
        return None
    return (num - 1) // 10


def divide_2(num: int):
    if num % 2 != 0:
        return None
    return num // 2


def bfs(num, target):
    result = 0
    queue = deque()
    queue.append(num)

    while queue:
        now = queue.popleft()
        result += 1

        if now == target:
            return result

        if now < target:
            continue

        special_result = special_calc(now)
        half = divide_2(now)

        if special_result is not None:
            queue.append(special_result)
        if half is not None:
            queue.append(half)

    return -1


a, b = map(int, input().split())
print(bfs(b, a))
