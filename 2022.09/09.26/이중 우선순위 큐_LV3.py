import heapq


def solution(operations):
    max_heap = []
    min_heap = []

    for item in operations:
        op = item.split()
        num = int(op[1])

        if op[0] == "I":
            if len(min_heap) == 0 or len(max_heap) == 0:
                heapq.heappush(max_heap, -num)
                heapq.heappush(min_heap, num)
            else:
                if min_heap[0] > num:
                    heapq.heappush(min_heap, num)
                if -max_heap[0] > -num:
                    heapq.heappush(max_heap, -num)
        else:
            if num == -1 and min_heap:
                heapq.heappop(min_heap)
                if len(min_heap) == 0 and len(max_heap) > 0:
                    heapq.heappop(max_heap)
            elif num == 1 and max_heap:
                heapq.heappop(max_heap)
                if len(max_heap) == 0 and len(min_heap) > 0:
                    heapq.heappop(min_heap)

    if len(min_heap) != 0 and len(max_heap) != 0:
        return [-max_heap[0], min_heap[0]]
    else:
        return [0, 0]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(
    solution(
        ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    )
)
