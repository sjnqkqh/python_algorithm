import bisect

n = int(input())
arr = list(map(int, input().split()))

dp = [int(1e9)]

for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        a = bisect.bisect_left(dp, arr[i])
        dp[a] = arr[i]

print(len(dp))
