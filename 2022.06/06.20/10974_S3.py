# URL : https://www.acmicpc.net/problem/10974
import itertools

n = int(input())

arr = [i for i in range(1, n + 1)]
result = []
permutation = itertools.permutations(arr)

for item in permutation:
    result.append(list(item))

for item in result:
    for val in item:
        print(val, end=" ")
    print()