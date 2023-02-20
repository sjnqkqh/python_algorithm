# 그래프에서 사이클이 존재하지 않으며 가장 짧은 거리를 갖는 '최소 신장 트리' 를 만드는 알고리즘

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


v, e = map(int, input().split(' '))
parent = []
for i in range(v+1):
    parent.append(i)

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split(' '))
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
