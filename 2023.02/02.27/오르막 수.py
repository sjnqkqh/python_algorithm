n = int(input())
# n = 4
dp = [[0] * (10) for _ in range(n + 1)]

for i in range(10):
    dp[1][i] = 1

for i in range(1, n + 1):
    dp[i][0] = 1

for i in range(1, n + 1):
    for j in range(1, 10):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 10007

print(sum(dp[n]) % 10007)
