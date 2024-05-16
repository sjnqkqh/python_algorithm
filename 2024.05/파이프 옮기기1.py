import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = 0
status = 0  # 파이프의 상태
vector = {0: [[0, 1, 0], [1, 1, 1]],
          1: [[0, 1, 0], [1, 0, 2], [1, 1, 1]],
          2: [[1, 0, 2], [1, 1, 1]]}  # i 증가값, j 증가값, 이동후 파이프 상태


def dfs(now_i, now_j, _status, visited: [[]]):
    global result
    next_vector = vector.get(_status)

    if now_i == n - 1 and now_j == n - 1:
        result += 1
        return

    for i, j, stat in next_vector:
        if stat == 1:
            if movable_right_under(now_i, now_j, visited):
                visited[now_i + i][now_j + j] = True
                dfs(now_i + i, now_j + j, stat, visited)
                visited[now_i + i][now_j + j] = False
        else:
            if (now_i + i < n and now_j + j < n
                    and arr[now_i + i][now_j + j] == 0
                    and not visited[now_i + i][now_j + j]):
                visited[now_i + i][now_j + j] = True
                dfs(now_i + i, now_j + j, stat, visited)
                visited[now_i + i][now_j + j] = False

    return


def movable_right_under(now_i, now_j, visited):
    if (now_i + 1 < n and now_j + 1 < n
            and not visited[now_i + 1][now_j + 1]
            and arr[now_i + 1][now_j + 1] == 0
            and arr[now_i + 1][now_j] == 0
            and arr[now_i][now_j + 1] == 0):
        return True
    return False


dfs(0, 1, 0, [[False] * n for _ in range(n)])
print(result)
