import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(6):
    arr.append([0, 0])

pre_left, pre_right = '', ''
for _ in range(n):
    left, right = map(int, input().split(' '))
    if arr[left][0] == 0 or left in [pre_left, pre_right]:
        arr[left][0] += 1

    if left != right:
        if arr[right][0] == 0 or right in [pre_left, pre_right]:
            arr[right][0] += 1

    arr[left][1] = max(arr[left])
    arr[right][1] = max(arr[right])

    for i in range(6):
        if i not in [left, right]:
            arr[i][0] = 0

    pre_left, pre_right = left, right

idx, max_cnt = 0, 0
for i in range(1, 6):
    if max_cnt < arr[i][1]:
        idx = i
        max_cnt = arr[i][1]

print(max_cnt, idx)
