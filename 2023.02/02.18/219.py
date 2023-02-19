n = int(input())
dp = [1e9] * (n+1)
dp[0], dp[1] = 0, 1

if n >= 2:
    dp[2] = 3

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp)
