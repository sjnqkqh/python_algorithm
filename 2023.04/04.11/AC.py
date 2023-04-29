from collections import deque


def solution(arr, orders):
    cursor = True
    if arr[0] == '':
        if 'D' in orders:
            return "error"
        else:
            return list()

    for order in orders:
        if order == "R":
            cursor = not cursor
        else:
            if len(arr) == 0:
                return "error"

            if cursor:
                arr.popleft()
            else:
                arr.pop()

    if not cursor:
        arr.reverse()

    return list(map(int, arr))


T = int(input())
for _ in range(T):
    orders = list(input())
    n = int(input())
    arr = deque(list(input().split(",")))

    arr[0] = arr[0].removeprefix("[")
    arr[-1] = arr[-1].removesuffix("]")

    result = solution(arr, orders)
    if result == 'error':
        print(result)
    else:
        print('[',end='')
        print(*result, sep = ',', end='')
        print(']')
