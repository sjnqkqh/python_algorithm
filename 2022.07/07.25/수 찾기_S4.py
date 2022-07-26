import heapq

N = int(input())
target_arr = list(map(int, input().split()))
M = int(input())
test_arr = list(map(int, input().split()))


# Heap Sort
temp_arr = []
for target in target_arr:
    heapq.heappush(temp_arr, target)

target_arr = [-1] * N
for i in range(N):
    temp = heapq.heappop(temp_arr)
    target_arr[i] = temp


def binary_search(num):
    low = 0
    high = N - 1
    mid = (low + high) // 2

    while high >= low:
        if target_arr[mid] == num:
            return True

        elif target_arr[mid] > num:
            high = mid - 1
            mid = (low + high) // 2

        elif target_arr[mid] < num:
            low = mid + 1
            mid = (high + low) // 2

    return False


for item in test_arr:
    if binary_search(item):
        print(1)
    else:
        print(0)
