import sys

input = sys.stdin.readline()

n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))