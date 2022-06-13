# URL : https://www.acmicpc.net/problem/2960

n, k = map(int, input().split())
arr = [i for i in range(n + 1)]
cnt = 0

for i in range(2, n + 1):
    for j in range(1, n):
        if i * j < n + 1 and arr[i*j] != 0:
            cnt = cnt + 1

            if cnt == k:
                print(arr[i*j])
                break

            arr[i * j] = 0
