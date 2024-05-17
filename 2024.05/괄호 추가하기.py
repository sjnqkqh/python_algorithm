n = int(input())
str = input()
dp = [-int(1E9)] * n
arr = []

for i in range(n):
    if i % 2 == 0:
        arr.append(int(str[i]))
    else:
        arr.append(str[i])


def calc(now, target, v):
    if v == '+':
        return target + now
    elif v == '-':
        return target - now
    else:
        return target * now


dp[0] = arr[0]
if n > 1:
    dp[1] = dp[0]
    dp[2] = calc(arr[2], arr[0], arr[1])

for i in range(4, n, 2):
    dp[i] = max(calc(arr[i], dp[i - 2], arr[i-1]),
                calc(dp[i - 4], calc(arr[i], arr[i - 2], arr[i-1]), arr[i-3]))

    print(dp)
