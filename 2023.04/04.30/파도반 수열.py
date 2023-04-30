dp = [0] * 101

dp[1], dp[2] = 1, 1

for i in range(3, 101):
    dp[i] = dp[i - 3] + dp[i - 2]

T = int(input())
for _ in range(T):
    print(dp[int(input())])
