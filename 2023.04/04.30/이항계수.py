n, k = map(int, input().split())
dp = [[0] * 1001 for _ in range(1001)]

for i in range(1001):
    dp[i][i] = 1
    dp[i][0] = 1

for i in range(1, 1001):
    for j in range(1, 1001):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007

print(dp[n][k])
