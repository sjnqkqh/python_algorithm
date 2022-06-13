# Page 149
from collections import deque

n, m = map(int, input().split())

# 얼음칸과 헤아린 얼음칸 생성
graph = []
visited = [[False] * m for _ in range(n)]

# 얼음칸 입력 받기
for i in range(n):
    graph.append(list(map(int, input().split())))


# 연속해서 인접한 노드 탐색(bfs)
def bfs(graph, start_x, start_y, visited):
    # 방문 처리
    queue = deque([[start_x, start_y]])
    visited[start_x][start_y] = True

    print(queue)
    print(visited)

    while queue:
        loc = queue.popleft()
        x = loc[0]
        y = loc[1]

        for i in graph:
            for j in graph[x]:
                # if not visited[i][j]:
                print(i)
                #     queue.append([i, j])
                #     visited[i][j] = True


bfs(graph, 0, 0, visited)
