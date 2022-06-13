# URL : https://www.acmicpc.net/problem/1463

n = int(input())

d = [0 for i in range(n + 1)]
divisorList = [3, 2]

# 범위가 2혹은 3을 넘어가는 시점에서 불변하는 초기값 세팅

if n >= 2:
    d[2] = 1
if n >= 3:
    d[3] = 1

# 최솟값 계산
for i in range(3, n + 1):
    d[i] = d[i - 1] + 1
    for divisor in divisorList:
        if i % divisor == 0:
            d[i] = min(d[i], d[i // divisor] + 1)

print(d[n])
