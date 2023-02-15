# URL : https://www.acmicpc.net/problem/1748
import math

n = int(input())
result = 0

log10 = int(math.log10(n))

for i in range(log10, -1, -1):
    # n이 10보다 클 때
    if i >= 1:
        minus = n - (10**i) + 1
        result = result + ((minus) * (i + 1))
        n = n - minus
    else:
        result = result + n

print(result)
