# URL : https://www.acmicpc.net/problem/14467

n = int(input())  # 1~100 정수

d = [-1 for i in range(n + 1)]
result = 0

for _ in range(1, n + 1):
    cowNumber, direction = map(int, input().split())
    if d[cowNumber] == -1:
        d[cowNumber] = direction

    if d[cowNumber] != -1 and d[cowNumber] != direction:
        result = result + 1
        d[cowNumber] = direction

print(result)
