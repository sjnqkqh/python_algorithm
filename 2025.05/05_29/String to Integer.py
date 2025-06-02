from collections import deque


def myAtoi(s: str) -> int:
    result = 0
    queue = deque(list(s))
    print(queue)

    while queue and queue[0] == ' ':
        queue.popleft()

    negative = False
    if queue and (queue[0] == '-' or queue[0] == '+'):
        now = queue.popleft()
        negative = True if now == '-' else False

    while queue and result == 0 and queue[0] == '0':
        queue.popleft()

    while queue and queue[0].isdigit():
        now = queue.popleft()
        result = result * 10 + int(now)

        if not negative:
            if result > 2 ** 31 - 1:
                return 2 ** 31 - 1
        else:
            if result > 2 ** 31:
                return - 2 ** 31

    result = result if not negative else -1 * result

    return result


print(myAtoi('-+12'))
