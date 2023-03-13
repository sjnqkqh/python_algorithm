n, k = map(int, input().split())
num = 1
while n > num * 2:
    n -= num * 2

print(n)
