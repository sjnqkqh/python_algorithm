import sys

N, M = map(int, input().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))


def combination_with_repeat(combine: list, m, level):
    if level == m:
        print(*combine, end=" ")
        print()
        return

    for num in arr:
        if len(combine) == 0 or num >= combine[-1]:
            combine.append(num)
            combination_with_repeat(combine, M, level + 1)
            combine.pop()


combination_with_repeat([], M, 0)
