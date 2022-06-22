# URL : https://www.acmicpc.net/problem/11724
from collections import deque

n, m = map(int, input().split())  # 정점의 개수
graph = [[] for _ in range(n + 1)]  # 그래프 배열 선언
result = 0

# 그래프 입력
for i in range(m):
    line = list(map(int, input().split()))
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])


# BFS 탐색 함수
def bfs(graph: list, start: int, visited: list):
    queue = deque()
    visited[start] = True
    queue.append(start)

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 연결 노드를 구하려면, DFS/BFS로 그래프를 순회한 다음, 아직 순회하지 않은 요소가 있는지 확인한다. (DFS/BFS로는 연결 요소를 넘어갈 수 없기에)
# 만약 탐색 이후에 방문하지 않은 노드가 있다면, 해당 노드로 시작점을 옮기고 연결 요소의 갯수를 1 증가시킨다.
visited = [False] * (n + 1)
visit_point_remain = True
start = 1

# 방문하지 않은 노드가 있는지 확인
while visit_point_remain:
    bfs(graph, start, visited)
    result += 1
    visit_point_remain = False

    # 방문하지 않은 정점이 있다면 시작점을 옮기고 BFS 반복
    for i in range(1, len(visited)):
        if not visited[i]:
            visit_point_remain = True
            start = i
            break

print(result)
