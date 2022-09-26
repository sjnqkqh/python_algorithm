import heapq
from collections import deque


def solution(jobs):
    answer = 0
    time = 0
    job_arr = []

    job_queue = deque(sorted(jobs, key=lambda x: x[0]))  # 입력 순서가 빠른 순으로 나열

    while True:
        # 모든 작업이 수행된 경우 케이스 종료
        if len(job_queue) == 0 and len(job_arr) == 0:
            break

        # 수행 가능한 작업 목록 선별
        while job_queue and time >= job_queue[0][0]:
            job = job_queue.popleft()
            heapq.heappush(job_arr, (job[1], job[0]))

        # 수행하야할 작업 (남은 시간이 가장 짧은)
        if job_arr:
            job = heapq.heappop(job_arr)
            time += job[0]
            answer += time - job[1]
            continue
        else:
            time += 1

    return int(answer / len(jobs))


print(solution([[0, 3], [1, 9], [2, 6]]))
