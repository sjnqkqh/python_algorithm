import heapq


def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)

    for _ in range(len(h)):
        result.append(-heapq.heappop(h))

    return result


result = heapsort([3, 2, 1])
print(result)
