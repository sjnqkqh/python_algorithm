# URL : https://www.acmicpc.net/problem/7562

from collections import deque


# BFS 탐색
def bfs(graph, x, y, visited):
    queue = deque()
    queue.append([y, x, 0])  # 3번째 항은 이동하는데 소요되는 턴

    while queue:
        v = queue.popleft()
        now_x = v[1]
        now_y = v[0]
        turn = v[2]

        # 현재 인덱스를 방문한 적이 있다면 다음 노드 탐색
        if visited[now_y][now_x]:
            continue

        visited[now_y][now_x] = True
        graph[now_y][now_x] = turn  # 이번칸까지 이동시 소요되는 횟수

        for move in move_arr:
            next_x = now_x + move[1]  # 다음 X 좌표
            next_y = now_y + move[0]  # 다음 Y 좌표

            if 0 <= next_x < n and 0 <= next_y < n and not visited[next_y][next_x]:
                queue.append([next_y, next_x, turn + 1])


# 이동 가능 경로
move_arr = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

time = int(input())  # 테스트 케이스 갯수
for _ in range(time):
    n = int(input())  # 체스판 길이
    graph = [[0 for _ in range(n)] for _ in range(n)]  # 체스판
    visited = [[False for _ in range(n)] for _ in range(n)]  # 방문 체크 배열
    start_x, start_y = map(int, input().split())  # 시작점 위치 (Y, X)
    x, y = map(int, input().split())  # 도착점 위치(Y, X)

    bfs(graph, start_x, start_y, visited)
    print(graph[y][x])
