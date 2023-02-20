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


# 문제 조건 입력
n, m = map(int, input().split(' '))
road = []
for _ in range(m):
    a, b, c = map(int, input().split(' '))
    road.append((c, a, b))
road.sort()

# 부모 노드 세팅
parent = []
for i in range(n + 1):
    parent.append(i)

# 하나의 최소 신장 트리를 만들고, 이 중에서 가장 비용이 큰 간선을 제거하여 2개의 마을로 분리
chosen_road = []
for item in road:
    cost, a, b = item
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        chosen_road.append(item)

result = 0
for item in chosen_road:
    result += item[0]
result -= chosen_road[-1][0]

print(result)