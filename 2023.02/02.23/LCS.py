import copy
import sys
from collections import deque

# input = sys.stdin.readline()
arr_1 = input()
arr_2 = input()
queue = deque()


def check(index_list):
    idx = 0
    for spell_idx in index_list:
        if len(arr_2) > idx >= 0:
            try:
                idx = arr_2[idx:].index(arr_1[spell_idx])
            except ValueError:
                return False

    return True


def make_after(origin: list, index):
    if index == len(arr_1):
        return

    for i in range(index + 1, len(arr_1)):
        copy_list = origin.copy()
        copy_list.append(i)
        if check(copy_list):
            queue.append(copy_list)


for i in range(len(arr_1)):
    queue.append([i])

result = -1
while queue:
    index_list: list = queue.popleft()

    result = max(result, len(index_list))
    make_after(index_list, index_list[-1])
print(result)
