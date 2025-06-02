T = int(input())
arr = []
for _ in range(T):
    arr.append(int(input()))

dp = [0, 1, 2, 4, 7]

for i in range(5, 11):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

for item in arr:
    print(dp[item])
