# URL : https://www.acmicpc.net/problem/15990
import math

n = int(input())
dp = [0 for _ in range(n + 1)]
arr = [[0, 0], [2, 1]]
dp[1] = 9

if n > 1:
    dp[2] = 17

result = 0

li = []


def get_number(number: int, cnt: int, remain: int):
    pre_number = number % 10
    if remain > 1:
        if pre_number != 9:
            get_number((number * 10) + pre_number + 1, cnt, remain - 1)
        if pre_number != 0:
            get_number((number * 10) + pre_number - 1, cnt, remain - 1)
    else:
        li.append(number)


for i in range(1, 10):
    now = i
    get_number(i, n, n)

print(len(li))
