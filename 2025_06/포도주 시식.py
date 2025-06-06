n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = []
for _ in range(n):
    dp.append([0, 0, 0])

dp[0] = [0, arr[0], arr[0]]
if n>1:
    dp[1] = [dp[0][2], arr[1], arr[0] + arr[1]]
if n>2:
    dp[2] = [dp[1][2], arr[0] + arr[2], arr[1] + arr[2]]

for i in range(3, n):
    dp[i] = [
        max(dp[i - 1]),
        dp[i - 1][0] + arr[i],
        dp[i - 1][1] + arr[i]
    ]

print(max(dp[n-1]))
