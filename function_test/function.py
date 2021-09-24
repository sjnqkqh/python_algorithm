import sys

# list(map(int, input().split()))
#
# it's equal. but faster than list(map(int, input().split()))
# sys.stdin.readline().rstrip()

# answer = 7
# print(f"정답은{answer}입니다!")

from itertools import permutations
from itertools import combinations

arr = ["A","B","C"]
result1 = list(permutations(arr, 2))

print(result1)

result2 = list(combinations(arr, 2))
print(result2)