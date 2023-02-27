import sys

input = sys.stdin.readline
arr1 = list(input().rstrip())
arr2 = list(input().rstrip())
len1, len2 = len(arr1) + 1, len(arr2) + 1

dp = [[0] * (len2) for _ in range(len1)]

for i in range(1, len1):
    for j in range(1, len2):
        if arr1[i - 1] == arr2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
