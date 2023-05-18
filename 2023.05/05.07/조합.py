from math import factorial

n, c = map(int, input().split())
result = factorial(n) // (factorial(n - c) * factorial(c))
print(result)
