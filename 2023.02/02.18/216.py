n = int(input())
arr = list(map(int, input().split(" ")))
max_arr = [-1] * n
max_arr[0], max_arr[1] = arr[0], max(arr[0], arr[1])

for i in range(2, n):
    max_arr[i] = max(max_arr[i-2]+arr[i], max_arr[i-1])

print(max_arr)