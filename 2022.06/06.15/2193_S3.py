# URL : https://www.acmicpc.net/problem/2193
# 문제를 잘못이해해서 dp[1]을 0으로 설정했었음. 이 경우에 1이 이친수라, dp[1] = 1

n = int(input())

dp = [0 for _ in range(n + 1)]
if n >= 1:
    dp[1] = 1
if n >= 2:
    dp[2] = 1
if n >= 3:
    dp[3] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(int(dp[len(dp) - 1]))
