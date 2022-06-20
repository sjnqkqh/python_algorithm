# URL : https://www.acmicpc.net/problem/10972
import itertools

# n = int(input()) # 배열의 최대 인덱스 (N)
# arr = list(map(int, input().split()))

# maxIdx = arr.index(n)

# for i in range(n -1, -1, -1):

n = 4  # 배열의 최대 인덱스 (N)
arr = [1, 2, 4, 3]

p = itertools.permutations(arr)
