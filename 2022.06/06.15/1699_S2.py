# URL : https://www.acmicpc.net/problem/1699
import math

n = int(input())

dp = [0 for _ in range(n + 1)]
dp[1] = 1

if n >= 2:
    dp[2] = 2

for i in range(3, n + 1):
    if math.sqrt(i) == int(math.sqrt(i)):  # i가 제곱수라면 항은 1
        dp[i] = 1
    else:
        li = [999999999]
        pivot = int(math.sqrt(i)) ** 2
        li.append(dp[pivot] + dp[i - pivot])

        li.append(dp[i - (i // 2)] + dp[i // 2])

        # 피벗값을 구해서 해당 값의 쌍 값과 더한 값도 최솟값 후보에 추가
        li.append(dp[pivot] + dp[i - pivot])
        dp[i] = min(dp[i - 1] + 1, min(li))

print(dp)
