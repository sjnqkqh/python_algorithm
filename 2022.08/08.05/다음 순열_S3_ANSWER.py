N = int(input())
arr = list(map(int, input().split()))

if arr == sorted(arr, reverse=True):
    print(-1)
else:
    swap_x = 0
    swap_y = 0

    for i in range(N - 1, 0, -1):
        if arr[i] > arr[i - 1]:
            swap_x = i
            swap_y = i - 1
            break

    for j in range(N - 1, -1, -1):
        if arr[j] > arr[swap_y]:
            temp = arr[swap_y]
            arr[swap_y] = arr[j]
            arr[j] = temp
            break

    pre_arr = arr[:swap_x]
    post_arr = sorted(arr[swap_x:])

    pre_arr.extend(post_arr)
    print(*pre_arr, sep=" ")

