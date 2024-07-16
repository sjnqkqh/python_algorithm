import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = []
case = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for _ in range(k):
    case.append(list(map(int, input().split())))


def permutations(arr, r):
    result = []

    def backtracking(start):
        if start == r:
            result.append(arr[:start])

        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            backtracking(start + 1)
            arr[start], arr[i] = arr[i], arr[start]

    backtracking(0)
    return result


perms = permutations(case, k)
# turn_square(arr)


print(list(map(list,zip(*arr)))[::1])