# URL : https://www.acmicpc.net/problem/14501
import sys

n = int(input())
arr = []  # 상담 리스트
dp = [0 for _ in range(n + 2)]  # DP 리스트

# 상담 리스트 입력
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n + 2):
    todayFinishJob = [1, 0]

    for j in range(len(arr)):
        # 당일에 끝나는 작업이 있다면 전일 실적과, 상담 시작일까지의 수입 + 상담료를 합한 것 중 큰 것 선택
        # 2일엔 1일 실적 VS 2일에 끝나는 작업의 (누적 수당 + 작업 수당)
        # 해당일에 끝나는 작업이 여러개일 수 있음. # 수당이 더 큰 작업으로 교체하는 조건 적용해야 함
        if i == j + 1 + arr[j][0] and dp[i - todayFinishJob[0]] + todayFinishJob[1] < dp[i-arr[j][0]]+arr[j][1]:
            todayFinishJob = arr[j]

    dp[i] = max(dp[i - 1], dp[i - todayFinishJob[0]] + todayFinishJob[1])

print(dp[len(dp)-1])
