# URL : https://www.acmicpc.net/problem/15990

n = int(input())
arr = []
dp = [0 for i in range(n + 1)]
for _ in range(n + 1):
    arr.append(int(input()))

maxNum = max(arr)  # 입력된 테스트 케이스 중 가장 큰 수
dp[1] = 1
if n > 1:
    dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 3]
