n = int(input())
num_arr = [0] * (n+1)
num_arr[1] = 1
for _ in range(n - 1):
    a, b = map(int, input().split())

    if num_arr[a] == 0:
        num_arr[a] = b
    else:
        num_arr[b] = a

num_arr = num_arr[2:]
for item in num_arr:
    print(item)