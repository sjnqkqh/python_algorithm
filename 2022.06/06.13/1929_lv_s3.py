# URL : https://www.acmicpc.net/problem/1929
n, m = map(int, input().split())

arr = [i for i in range(0, m + 1)]

for i in range(2, m):
    if arr[i] != 0:
        for j in range(2, m):  # 곱해서 나올 수 있는 수 제거
            if i * j <= m:
                arr[i * j] = 0
            else:
                break

arr = arr[n : m + 1]
if 1 in arr:
    arr.remove(1)

for n in arr:
    if n:
        print(n)
