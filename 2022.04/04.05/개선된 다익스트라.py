import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한, 10억

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보 리스트
graph = [[] for i in range(n + 1)]

# 최단 거리 테이블 노드 전부 INF로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 노드에서 b까지 가는 거리가 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    # 시작 노드 초기화
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)

        # 현재 노드가 처리된 적이 있다면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 인접한 다른 노드를 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서 다른 노드로 가는 것이 더 빠를 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
