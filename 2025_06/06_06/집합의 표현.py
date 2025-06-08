import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n += 1
parent = [0] * n

for i in range(n):
    parent[i] = i


def find_parent(a):
    path = []
    while a != parent[a]:
        path.append(a)
        a = parent[a]
    root = a
    for node in path:
        parent[node] = root
    return root



def union(a, b):
    a_parent = find_parent(a)
    b_parent = find_parent(b)

    min_num = min(a_parent, b_parent)
    parent[a_parent] = min_num
    parent[b_parent] = min_num

    parent[a] = min_num
    parent[b] = min_num


for i in range(m):
    show_trigger, a, b = map(int, input().split())
    if show_trigger:
        same = 'YES' if find_parent(a) == find_parent(b) else 'NO'
        print(same)
        continue

    union(a, b)
