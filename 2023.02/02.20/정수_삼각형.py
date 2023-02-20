n = int(input())
arr = [[] for _ in range(n)]
dp = [[] for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(i + 1):
        dp[i].append(0)

dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i + 1):
        cases = []

        if j == 0:
            cases.append(dp[i - 1][j])
        elif i > j > 0:
            cases.append(dp[i - 1][j])
            cases.append(dp[i - 1][j - 1])
        else:
            cases.append(dp[i - 1][j - 1])

        dp[i][j] = arr[i][j] + max(cases)

print(max(dp[n - 1]))
