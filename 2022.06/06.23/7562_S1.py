# URL : https://www.acmicpc.net/problem/7562

# BFS 탐색
from collections import deque


def bfs(graph, x, y, visited):
    queue = deque()
    visited[y][x] = True
    turn = 0
    queue.append([y, x, 0])  # 3번째 항은 이동하는데 소요되는 턴
    while queue:
        v = queue.popleft()
        print(v[0], v[1])
        visited[v[0]][v[1]] = True
        graph[v[0]][v[1]] = turn  # 이번칸까지 이동시 소요되는 횟수
        turn += 1  # 다음 칸까지 이동시 소요되는 횟수

        for move in move_arr:
            next_x = v[1] + move[1]  # 다음 X 좌표
            next_y = v[0] + move[0]  # 다음 Y 좌표

            if 0 <= next_x < n and 0 <= next_y < n and not visited[next_y][next_x]:
                queue.append([next_y, next_x, turn])


# 이동 가능 경로
move_arr = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

time = int(input())  # 테스트 케이스 갯수

n = int(input())  # 체스판 길이
graph = [[0] * n] * n  # 체스판
visited = [[False] * n] * n  # 방문 체크 배열
start_x, start_y = map(int, input().split())  # 시작점 위치 (Y, X)
x, y = map(int, input().split())  # 도착점 위치(Y, X)

bfs(graph, start_x, start_y, visited)
for i in graph:
    print(i)
