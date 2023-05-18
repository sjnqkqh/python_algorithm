# n = int(input())
n = 5


def blocking(arr: list, i, j):
    for k in range(n):
        arr[k][j] = False
        arr[i][k] = False

    k = 0
    while n > i + k >= 0 and n > j + k >= 0:
        arr[i + k][j + k] = False
        k += 1

    k = 0
    while i - k >= 0 and n > j + k:
        arr[i - k][j + k] = False
        k += 1

    k = 0
    while i - k >= 0 and j - k >= 0:
        arr[i - k][j - k] = False
        k += 1

    k = 0
    while n > i + k and j - k >= 0:
        arr[i + k][j - k] = False
        k += 1


def get_next(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                return (i, j)

    return False


arr = [[True] * n for _ in range(n)]
