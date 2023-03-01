import sys

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
dp = [0] * (n + 1)

dp[0] = arr[0]
if n > 1:
    dp[1] = dp[0] + arr[1]

for i in range(2, n):
    dp[i] = max(
        dp[i - 2] + arr[i],
        dp[i - 3] + arr[i - 1] + arr[i]
    )

print(dp[n - 1])
