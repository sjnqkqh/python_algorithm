n = int(input())

dp = [int(1e9)] * (n + 1)
dp[0] = 0
dp[1] = 0
for i in range(2, n + 1):
    list = [dp[i - 1] + 1]
    if i % 2 == 0:
        list.append(dp[i // 2] + 1)
    if i % 3 == 0:
        list.append(dp[i // 3] + 1)
    dp[i] = min(list)

print(dp[-1])
