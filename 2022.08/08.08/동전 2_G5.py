N, K = map(int, input().split())
arr = set()
dp = [int(1e9)] * (K + 1)
dp[0] = 0

for _ in range(N):
    arr.add(int(input()))
arr = sorted(list(arr))

for i in range(arr[0], K + 1):
    for j in range(len(arr)):
        if 0 <= i - arr[j] < K:
            dp[i] = min(dp[i - arr[j]] + 1, dp[i])

print(dp[K] if dp[K] != int(1e9) else -1)
