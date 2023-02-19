n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [int(1e9)] * (m + 1)

for token in arr:
    if token < m:
        dp[token] = 1

    for i in range(m+1):
        if i-token >= 0:
            dp[i] = min(dp[i], dp[i-token]+1)

print(dp[m] if dp[m] != int(1e9) else -1)
