n = int(input())
arr = list(map(int, input().split(' ')))

dp = [0] * n

dp[0] = max(arr[0], 0)
for i in range(n):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])

print(max(dp))