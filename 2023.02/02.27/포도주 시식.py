n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [0] * (n + 1)
dp[0] = arr[0]
dp[1] = dp[0] + arr[1]

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

print(arr)
print(dp)
