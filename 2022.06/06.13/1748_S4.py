# URL : https://www.acmicpc.net/problem/1748
import math

n = int(input())
result = 0
now = n

for i in range(8, -1, -1):
    div = int(math.pow(10, i))
    print(div)
    if now >= div:
        result =



print(result)
