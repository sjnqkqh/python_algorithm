from collections import deque

move_arr = [[0, 0, 1], [0, 0, -1], [1, 0, 0], [0, 1, 0], [-1, 0, 0], [0, -1, 0]]
n, m, h = map(int, input().split())


def find_good_tomato():
    queue = deque()
    for i in range(m):
        for j in range(n):
            for k in range(h):
                if array[k][i][j] == 1 and not visited[k][i][j]:
                    queue.append([k, i, j])

    return queue


def find_remain_tomato(bfs_result):
    for i in range(m):
        for j in range(n):
            for k in range(h):
                if array[k][i][j] == 0:
                    return -1

    return bfs_result


def bfs():
    queue = find_good_tomato()
    result = 0
    next_queue = deque()

    while queue:
        k, i, j = queue.popleft()
        visited[k][i][j] = True

        for move in move_arr:
            next_k, next_i, next_j = k + move[0], i + move[1], j + move[2]
            if (
                    0 <= next_i < m
                    and 0 <= next_j < n
                    and 0 <= next_k < h
                    and not visited[next_k][next_i][next_j]
                    and array[next_k][next_i][next_j] == 0
            ):
                next_queue.append([next_k, next_i, next_j])
                visited[next_k][next_i][next_j] = True
                array[next_k][next_i][next_j] = 1

        if len(queue) == 0 and next_queue:
            queue = next_queue
            next_queue = deque()
            result += 1

    return result


array = [[] * n for _ in range(h)]
visited = [[[False] * n for _ in range(m)] for _ in range(h)]

for i in range(h):
    for j in range(m):
        array[i].append(list(map(int, input().split())))

bfs_result = find_remain_tomato(bfs())
print(bfs_result)
