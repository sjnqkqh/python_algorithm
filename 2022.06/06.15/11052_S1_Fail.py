# URL : https://www.acmicpc.net/problem/11052

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = n * arr[0]

payPerPaper = []
for i in range(n):
    payPerPaper.append(arr[i] / (i + 1))

print(max(payPerPaper))
print(payPerPaper.index(max(payPerPaper)))

maxIdx = payPerPaper.index(max(payPerPaper))

for i in range(1, n):
    # dp[i] = max(dp[i - 1] + arr[0], arr[i],
    #             dp[n // i] * (n // i) + dp[n - (n // i)])
    li = []
    for j in range(i):
        li.append(arr[j] + dp[i - j])
    print("li", li)
    #
    if i >= maxIdx:
        print(dp[i - 1] + arr[0], i - maxIdx, dp[i - maxIdx] + dp[maxIdx], arr[i])
        dp[i] = max(dp[i - 1] + arr[0], dp[i - maxIdx] + dp[maxIdx], arr[i])
    else:
        dp[i] = max(dp[i - 1] + arr[0], arr[i])


print(dp)
