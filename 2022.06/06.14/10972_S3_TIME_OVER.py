# URL : https://www.acmicpc.net/problem/10972
import itertools

n = int(input())
arr = list(map(int, input().split()))  # 검색할 순영
nums = list([i for i in range(1, n + 1)])

permutations = itertools.permutations(nums)

for p in permutations:
    if arr == list(p):
        try:
            nextPermutation = permutations.__next__()
            for item in nextPermutation:
                print(item, end=' ')
        except StopIteration:
            print("-1")
