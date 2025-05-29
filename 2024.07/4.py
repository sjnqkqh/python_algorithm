from collections import deque


def solution(arr: list):
    result = 0
    arr.sort()
    arr = deque(arr)
    next_step = deque()

    while arr:
        pre_num = 0

        origin_length = len(arr)
        for i in range(len(arr)):
            now = arr.popleft()
            if now > pre_num != 0:
                result += 1
            elif now == pre_num:
                next_step.append(now)

            pre_num = now

        if origin_length == len(next_step):
            return result

        arr = next_step

    return result
