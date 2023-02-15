# URL : https://www.acmicpc.net/problem/15651
import itertools

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]

result = itertools.product(arr, repeat=m)

for item in result:
    for i in item:
        print(i, end=" ")
    print()
