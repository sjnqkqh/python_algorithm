import sys

N = int(input())
ownArr = list(map(int, sys.stdin.readline().split()))
M = int(input())
targetArr = list(map(int, sys.stdin.readline().split()))

num_dict = dict()
for item in ownArr:
    if num_dict.get(item) is None:
        num_dict[item] = 1
    else:
        num_dict[item] = num_dict[item] + 1

for item in targetArr:
    val = num_dict.get(item)
    print(val if val is not None else 0, end=' ')
