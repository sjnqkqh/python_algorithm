# URL : https://www.acmicpc.net/problem/13023
from collections import deque


def dfs(graph: list, idx, link_cnt, passed: list):
    if link_cnt == 5:
        return True

    passed.append(idx)
    friends = graph[idx]

    print("link:", link_cnt)
    print("idx:", idx)
    print("friends:", friends)
    print("passed:", passed)
    print()

    for item in friends:
        if item not in passed:
            link_cnt += 1
            passed.append(item)
            dfs(graph, item, link_cnt + 1, passed)

    return False


# DFS 탐색
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
passed = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(graph, 0, 0, passed))

# 2 7 4 3 5
