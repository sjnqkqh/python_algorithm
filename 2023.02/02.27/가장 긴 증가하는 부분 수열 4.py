import heapq
import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

length = max(dp)
max_num = 1000000000000
result = []

for target in range(length, -1, -1):
    target_list = []
    for i in range(n):
        if dp[i] == target:
            heapq.heappush(target_list, -arr[i])

    while target_list:
        item = -heapq.heappop(target_list)
        if item < max_num:
            result.append(item)
            max_num = item
            break

result.reverse()

print(length)
print(*result, sep=' ')