# URL : https://www.acmicpc.net/problem/1748
import math

n = int(input())
result = 0
now = n

for i in range(0, 9):
    div = math.pow(10, i)

    result = now

print(result)
