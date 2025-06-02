t = int(input())
arr = []
for _ in range(t):
    arr.append(int(input()))

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4, len(dp)):
    dp[i] = dp[i - 2] + dp[i - 3]

for item in arr:
    print(dp[item])
