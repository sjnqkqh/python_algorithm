from collections import deque
from queue import PriorityQueue


def solution(jobs):
    total_consume_time = 0
    done = [False for _ in range(len(jobs))]
    jobs.sort(key=lambda x: x[1])

    time = 0
    while True:
        if False in done:
            pass
        else:
            return total_consume_time // len(jobs)

        job = []
        for i in range(len(jobs)):
            if jobs[i][0] <= time and not done[i]:
                job = jobs[i]
                done[i] = True
                break

        if len(job) == 0:
            time += 1
        else:
            total_consume_time += job[1] + time - job[0]
            time += job[1]


print(solution(	[[0, 3], [1, 9], [2, 6]]))
