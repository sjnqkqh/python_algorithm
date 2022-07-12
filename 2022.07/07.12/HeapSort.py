import heapq


def heapSort(iterable):
    h = []
    result = []
    for val in iterable:
        heapq.heappush(h, val)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


h = [1, 53, 7, 83, 54, 8, 21, 5684, 524, 87, 856, 85, 46, 54, 65]
sorted = heapSort(h)

print(sorted)
