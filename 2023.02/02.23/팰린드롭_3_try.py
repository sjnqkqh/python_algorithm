import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

dp = [[False] * n for _ in range(n)]

for i in range(n):
    for start in range(n - i):
        end = start + i
        if start == end:
            dp[start][end] = True
        elif numbers[start] == numbers[end]:
            if start + 1 == end:
                dp[start][end] = True
            elif dp[start + 1][end - 1]:
                dp[start][end] = True

for i in range(m):
    s, e = map(int, input().split())
    if dp[s - 1][e - 1]:
        print(1)
    else:
        print(0)
