# URL : https://www.acmicpc.net/problem/15656
import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))

products = list(itertools.product(arr, repeat=m))
products.sort()

for product in products:
    for var in product:
        print(var, end=" ")
    print()
