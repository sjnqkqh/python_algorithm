from collections import deque

n = int(input())
subjects = []
visited = [False] * (n + 1)

# 과목 입력
for i in range(1, n + 1):
    subject = list(map(int, input().split()))
    pre_subjects = []
    for j in range(1, len(subject) - 1):
        pre_subjects.append(subject[j])
    subjects.append([i, subject[0], pre_subjects, 0])

# 차수 설정
queue = deque()
for subject in subjects:
    if len(subject[2]) == 0:
        queue.append(subject)
        visited[subject[0]] = True

# 강의 시간 계산
while queue:
    subject_id, cost, pre_subjects, pre_result = queue.popleft()

    for subject in subjects:
        if subject_id in subject[2]:
            subject[2].remove(subject_id)
            subject[3] = cost + pre_result

        if len(subject[2]) == 0 and not visited[subject[0]]:
            queue.append(subject)
            visited[subject[0]] = True

# 총 강의 시간 출력
for item in subjects:
    print(item[1]+item[3])
