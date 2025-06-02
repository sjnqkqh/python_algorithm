import math

n = int(input())
dp = [0] * 31
dp[2] = 3
dp[4] = 11

for i in range(6, 31, 2):
    dp[i] = dp[i - 2] * 3
    for j in range(i - 4, 0, -2):
        dp[i] += dp[j] * 2
    dp[i] += 2

print(dp[n])
