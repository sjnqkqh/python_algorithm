# URL : https://www.acmicpc.net/problem/10819
import itertools

n = int(input())
arr = list(map(int, input().split()))
permList = []
permutation = itertools.permutations(arr)

for item in permutation:
    permList.append(list(item))

result = []

maxNum = -1
for perm in permList:
    sum = 0
    for i in range(1, n):
        sum = sum + abs(perm[i - 1] - perm[i])
        maxNum = max(maxNum, sum)

print(maxNum)
