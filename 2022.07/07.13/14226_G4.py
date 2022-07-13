from collections import deque

# 초기 데이터 세팅
S = int(input())
arr = [[-1 for _ in range(S + 10)] for _ in range(S + 10)]
clip = 1  # 클립보드에 저장된 이모티콘의 수
now = 1  # 계산을 시작할 인덱스


# BFS 탐색
def bfs(clip, now):
    cnt = 1
    queue = deque()
    queue.append((clip, now))

    while queue:
        size = len(queue)
        for _ in range(size):
            clip, now = queue.popleft()

            # 목표 수치에 도달했다면 반복 종료
            if now == S:
                print(cnt)
                return

            # now - 1 인덱스까지 도달하는 계산 횟수 등록
            if arr[now - 1][clip] > cnt or arr[now - 1][clip] == -1:
                arr[now - 1][clip] = cnt + 1
                # print("arr[now({0}) - 1] = cnt:".format(now), cnt)
                queue.append((clip, now - 1))

            # now + clip 인덱스까지 도달하는 계산 횟수 등록
            if now + clip < S + 1 and arr[now + clip][clip] == -1:
                arr[now + clip][clip] = cnt + 1
                # print("arr[now({0}) + clip({1})] = cnt:".format(now, clip), cnt)
                queue.append((clip, now + clip))

                # 클립보드에 now를 복사
            if now > clip:
                queue.append((now, now))

        cnt += 1


bfs(clip, now)
