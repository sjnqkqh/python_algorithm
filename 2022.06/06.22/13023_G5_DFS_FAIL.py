# URL : https://www.acmicpc.net/problem/13023
import sys
sys.setrecursionlimit(10**6)

# DFS 탐색
def dfs(graph: list, idx, link_cnt, passed: list, finished: list, start):
    # 그래프의 모든 인원에 대한 검증이 끝났다면 False
    if start == n:
        return False

    # 탐색 과정에 대한 일시 방문처리
    passed.append(idx)
    friends = graph[idx]

    # 인덱스의 친구들 중, 탐색에서 지나치지 않은 노드를 방문
    for item in friends:
        if item not in passed:
            return dfs(graph, item, link_cnt + 1, passed, finished, start)

    # start에서 시작한 탐색 이후, 연결된 친구들이 5을 초과한다면 True
    if len(passed) >= 5:
        return True

    # 모든 조건이 불일치하면 다음 번호의 친구를 기준으로 탐색 시작
    if start < n:
        return dfs(graph, start + 1, 1, [], finished, start + 1)
    else:
        return False


# DFS 탐색
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
passed = []
finished = []
7
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(1 if dfs(graph, 0, 1, passed, finished, 0) else 0)
