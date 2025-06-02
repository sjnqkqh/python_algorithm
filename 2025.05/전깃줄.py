import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))
arr.sort()

lis = [1] * len(arr)

for i in range(1, len(arr)):
    idx = []
    max_num = 0
    for j in range(i):
        if arr[j][1] < arr[i][1]:
            idx.append(j)

    for k in idx:
        max_num = max(max_num, lis[k], lis[i])

    lis[i] = max_num + 1

print(n - max(lis))
