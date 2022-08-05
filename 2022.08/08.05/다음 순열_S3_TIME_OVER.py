import copy
import sys

sys.setrecursionlimit(10000)
N = int(input())
first = list(map(int, input().split()))
arr = sorted(first)
last = sorted(arr, reverse=True)

result = [0] * len(arr)
visited = [False] * len(arr)
stack = []
flag = False


def get_permutation(N, M, level):
    global flag
    if M == level:
        if len(stack) > 0:
            if stack[-1] == first:
                flag = True
                print(*result, sep=" ")
            else:
                stack.pop()

        stack.append(copy.deepcopy(result))
        return

    for i in range(N):
        if visited[i] is False:
            visited[i] = True
            result[level] = arr[i]
            get_permutation(N, M, level + 1)
            visited[i] = False

            if flag:
                return


if first == last:
    print(-1)
else:
    get_permutation(N, len(arr), 0)
