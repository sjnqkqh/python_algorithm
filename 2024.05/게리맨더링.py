# https://www.acmicpc.net/problem/14499
from collections import deque

result = 1E9
n = int(input())
man = list(map(int, input().split()))
arr = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp)):
        arr[i].append(temp[j] - 1)


def get_rest(visited: list):
    rest = []
    for i in range(n):
        if not visited[i]:
            rest.append(i)

    return rest


def check_a_group(start):
    visited = [False] * n
    visited[start] = True
    queue = deque([start])
    while queue:
        i = queue.popleft()
        visited[i] = True
        for item in arr[i]:
            if not visited[item]:
                queue.append(item)

    return visited


def dfs(visited, now):
    global result
    for next in arr[now]:
        if not visited[next]:
            visited[next] = True

            another_group_sum = get_group_sum(get_rest(visited))
            if another_group_sum > 0:
                origin_group = []
                for i in range(n):
                    if visited[i]:
                        origin_group.append(i)
                now_group_sum = get_group_sum(origin_group)
                result = min(result, abs(another_group_sum - now_group_sum))

            dfs(visited, next)
            visited[next] = False


def get_group_sum(_rest: list):
    if len(_rest) == 0:
        return -1
    _result = 0
    _visited = [False] * n
    queue = deque()
    queue.append(_rest[0])
    while queue:
        i = queue.popleft()
        if not _visited[i]:
            _visited[i] = True
            for item in arr[i]:
                if not _visited[item]:
                    queue.append(item)

    for item in _rest:
        if not _visited[item]:
            return -1

    for item in _rest:
        _result += man[item]

    return _result


first_group = check_a_group(0)
rest = []
for i in range(n):
    if not first_group[i]:
        rest.append(i)

# 모든 노드가 한 덩어리일 경우
if len(rest) == 0:
    for i in range(n):
        visited = [False] * n
        visited[i] = True
        dfs(visited, i)
    print(result)
    exit()

# 모든 노드가 2개의 그룹으로 나뉘는 경우
is_a_group = get_group_sum(rest)
if is_a_group > 0:
    origin_group = []
    for i in range(n):
        if i not in rest:
            origin_group.append(i)

    print(abs(get_group_sum(origin_group) - is_a_group))

else:
    # 모든 노드가 이미 3개 이상의 그룹으로 나뉜 경우
    print(-1)
