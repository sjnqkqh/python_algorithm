# URL : https://www.acmicpc.net/problem/9095

n = int(input())
arr = []

# 입력 받은 수의 리스트
for _ in range(n):
    arr.append(int(input()))

maxNumber = max(arr)  # 입력된 수 중 가장 큰 수 = DP 배열의 길이 - 1

dp = [0 for _ in range(maxNumber + 1)]

if maxNumber >= 1:
    dp[1] = 1
if maxNumber >= 2:
    dp[2] = 2
if maxNumber >= 3:
    dp[3] = 4

for i in range(4, maxNumber + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for index in arr:
    print(dp[index])
