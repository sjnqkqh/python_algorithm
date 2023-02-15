# URL : https://www.acmicpc.net/problem/15654
import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()  # 수열을 오름차순으로 세팅

permutations = itertools.permutations(arr, m)

for permutation in permutations:
    for item in permutation:
        print(item, end=" ")
    print()
