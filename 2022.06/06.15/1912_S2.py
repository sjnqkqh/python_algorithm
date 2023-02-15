# URL : https://www.acmicpc.net/problem/1912

n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n + 1)]
dp[1] = arr[0]

for i in range(2, n + 1):
    dp[i] = max(dp[i - 1] + arr[i - 1], arr[i - 1])

print(max(dp[1:]))
