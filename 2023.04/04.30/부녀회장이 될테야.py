T = int(input())

dp = [[0] * 15 for _ in range(15)]

for i in range(1, 15):
    dp[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

for _ in range(T):
    n = int(input())
    m = int(input())

    print(dp[n][m])