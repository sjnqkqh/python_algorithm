# URL : https://www.acmicpc.net/problem/11726

n = int(input())

result = 0
dp = [0 for i in range(n + 1)]

# 채워야 할 타일의 길이가 1인 경우
if n >= 1:
    dp[1] = 1
if n >= 2:
    dp[2] = 2

# 사용 방식 DP -> 이전 연산 결과에서 하나씩 점진적으로 해를 도출해가는 방법
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)
