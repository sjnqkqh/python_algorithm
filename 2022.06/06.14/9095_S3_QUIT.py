# URL : https://www.acmicpc.net/problem/9095
import itertools

T = int(input())
ans = 0


def plus(param, cnt, increase, limit):
    cnt = cnt + 1
    param = param + increase
    global ans
    ans = ans + 1

    if param + 1 <= limit:
        plus(param, cnt, 1, limit)
    if param + 2 <= limit:
        plus(param, cnt, 2, limit)
    if param + 3 <= limit:
        plus(param, cnt, 3, limit)
    if param == limit:
        cnt = cnt + 1

    return cnt


for _ in range(0, T):
    n = int(input())
    result = 0
    result = result + plus(0, 0, 1, n)
    result = result + plus(0, result, 2, n)
    result = result + plus(0, result, 3, n)

    print("ans", ans)
