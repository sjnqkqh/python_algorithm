import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n += 1
arr = [0] * n
for i in range(n):
    arr[i] = i

arr = [set()] * n
for i in range(n):
    arr[i] = {i}

for i in range(m):
    check_union, a, b = map(int, input().split())
    if check_union:
        if a in arr[b]:
            print("YES")
        else:
            print("NO")
        continue

    temp = arr[a].union(arr[b])
    arr[a] = temp
    arr[b] = temp
    for i in arr[a]:
        arr[i] = arr[a]
#
# for item in arr:
#     print(item)