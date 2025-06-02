n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))
dp = [0] * (k + 1)

for w, v in arr:
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(max(dp))
