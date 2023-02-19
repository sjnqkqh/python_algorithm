def get_min(number):
    min_arr = []
    if number % 5 == 0:
        min_arr.append(arr[number // 5] + 1)
    elif number % 3 == 0:
        min_arr.append(arr[number // 3] + 1)
    elif number % 2 == 0:
        min_arr.append(arr[number // 2] + 1)
    min_arr.append(arr[number-1] +1)

    return min(min_arr)


INF = int(10e9)
n = int(input())
arr = [INF] * (n+1)
arr[1] = 0

for i in range(2, n+1):
    arr[i] = min(arr[i], get_min(i))

print(arr[-1])