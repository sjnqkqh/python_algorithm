n = int(input())
int_str = input()
MIN = -int(2 ** 31)
MAX = int(2 ** 31)
max_dp = [MIN] * n
min_dp = [MAX] * n

arr = []

for i in range(n):
    if i % 2 == 0:
        arr.append(int(int_str[i]))
    else:
        arr.append(int_str[i])


def calc(now, target, v):
    if v == '+':
        return target + now
    elif v == '-':
        return target - now
    else:
        return target * now


max_dp[0] = arr[0]
min_dp[0] = arr[0]
if n >= 3:
    max_dp[1] = max_dp[0]
    max_dp[2] = calc(arr[2], arr[0], arr[1])
    min_dp[1] = max_dp[0]
    min_dp[2] = calc(arr[2], arr[0], arr[1])

for i in range(4, n, 2):
    max_dp[i] = max(
        calc(arr[i], max_dp[i - 2], arr[i - 1]),
        calc(arr[i], min_dp[i - 2], arr[i - 1]),
        calc(calc(arr[i], arr[i - 2], arr[i - 1]), max_dp[i - 4], arr[i - 3]),
        calc(calc(arr[i], arr[i - 2], arr[i - 1]), min_dp[i - 4], arr[i - 3]),
    )

    min_dp[i] = min(
        calc(arr[i], max_dp[i - 2], arr[i - 1]),
        calc(arr[i], min_dp[i - 2], arr[i - 1]),
        calc(calc(arr[i], arr[i - 2], arr[i - 1]), max_dp[i - 4], arr[i - 3]),
        calc(calc(arr[i], arr[i - 2], arr[i - 1]), min_dp[i - 4], arr[i - 3]),
    )

print(max(max_dp[-1], min_dp[-1]))
