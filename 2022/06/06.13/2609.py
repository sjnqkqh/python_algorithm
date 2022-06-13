# URL : https://www.acmicpc.net/problem/2609

import math

n, m = map(int, input().split())

maxDivisor = math.gcd(n, m)
minMultiple = (n * m) // maxDivisor

print(maxDivisor)
print(minMultiple)
