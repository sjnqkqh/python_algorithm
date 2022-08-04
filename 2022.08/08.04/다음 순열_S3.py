import copy

N = int(input())
arr = list(map(int, input().split()))
result = [0] * len(arr)
visited = [False] * len(arr)


def get_permutation(before, N, M, level):
    if M == level and before == arr:
        print(result)
        return

    for i in range(N):
        if visited[i] is False:
            visited[i] = True
            result[level] = arr[i]
            get_permutation(copy.deepcopy(result), N, M, level + 1)
            visited[i] = False


get_permutation([], N, len(arr), 0)
