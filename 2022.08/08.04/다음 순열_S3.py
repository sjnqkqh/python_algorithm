import copy

N = int(input())
arr = list(map(int, input().split()))
result = [0] * len(arr)
visited = [False] * len(arr)
flag = False


def get_permutation(N, M, level):
    global flag
    if M == level and result == arr:
        print(result)
        return

    for i in range(N):
        if visited[i] is False:
            visited[i] = True
            result[level] = arr[i]
            get_permutation(N, M, level + 1)
            visited[i] = False


get_permutation(N, len(arr), 0)
