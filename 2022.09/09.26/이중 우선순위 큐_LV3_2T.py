import heapq


def solution(operations):
    heap = []
    for item in operations:
        op = item.split()
        num = int(op[1])

        if op[0] == 'I':
            heapq.heappush(heap, num)
        else:
            if num == 1 and heap:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
            if num == -1 and heap:
                heapq.heappop(heap)

    if heap:
        if len(heap) == 1:
            return [heap[0], heap[0]]
        else:
            return [heapq.nlargest(1,heap)[0], heapq.heappop(heap)]
    else:
        return [0,0]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
#
