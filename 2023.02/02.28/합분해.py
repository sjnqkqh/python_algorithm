n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][1] = 1

for j in range(2, k + 1):
    for i in range(1, n + 1):
        for k in range(1, i+1):
            dp[i][j] += dp[k][j - 1]
            dp[i][j] = dp[i][j] % 1000000000

print(sum(dp[n]) % 1000000000)