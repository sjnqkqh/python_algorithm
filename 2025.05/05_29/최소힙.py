import heapq

N = int(input())
arr = []
min_heap = []
for i in range(N):
    num = int(input())
    if num == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, num)