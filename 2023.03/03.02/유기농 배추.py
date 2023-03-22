from collections import deque


def get_point():
    while visitable:
        i, j = visitable.pop()

        if arr[i][j]:
            return [i, j]

    return [-1, -1]


def bfs():
    result = 1
    queue = deque()
    i, j = get_point()
    queue.append([i, j])
    arr[i][j] = False

    while queue:
        i, j = queue.popleft()
        for move in move_arr:
            next_i, next_j = i + move[0], j + move[1]
            if 0 <= next_i < m and 0 <= next_j < n and arr[next_i][next_j]:
                arr[next_i][next_j] = False
                queue.append([next_i, next_j])

        if not queue and visitable:
            i, j = get_point()
            if i == -1 and j == -1:
                return result
            queue.append([i, j])
            result += 1

    return result


T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    arr = [[False] * n for _ in range(m)]
    visitable = []
    move_arr = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for _ in range(k):
        j, i = map(int, input().split())
        arr[i][j] = True
        visitable.append([i, j])

    result = bfs()

    print(result)
