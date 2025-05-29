import heapq
from collections import deque

hq = []


def solution(n, coffee_times):
    answer = []
    now = 0
    coffee_queue = deque()
    for i in range(len(coffee_times)):
        coffee_queue.append((coffee_times[i], i + 1))

    for i in range(min(n, len(coffee_queue))):
        time, num = coffee_queue.popleft()
        heapq.heappush(hq, (time + now, num))

    while hq:
        time, num = heapq.heappop(hq)
        answer.append(num)
        now = time

        if coffee_queue:
            next_time, next_num = coffee_queue.popleft()
            heapq.heappush(hq, (now + next_time, next_num))

    return answer