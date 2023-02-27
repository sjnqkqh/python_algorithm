import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
questions = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
for _ in range(m):
    questions.append(list(map(int, input().split())))

dp = arr[:]
for i in range(n):
    for j in range(1, n):
        dp[i][j] = dp[i][j - 1] + dp[i][j]

for item in questions:
    result = 0
    i1, j1, i2, j2 = map(lambda x: x - 1, item)
    for i in range(i1, i2 + 1):
        result += dp[i][j2]
        if j1 != 0:
            result -= dp[i][j1-1]

    print(result)
