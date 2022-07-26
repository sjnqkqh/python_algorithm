N = int(input())
M = int(input())
INF = int(0)
arr = dict()

parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i


# 부모 노드 탐색
def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]


# 집합 합치기
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    parent[root2] = root1


# 무방향 그래프 생성
for i in range(M):
    link = list(map(int, input().split()))
    arr[(link[0], link[1])] = link[2]

# 정렬
arr = sorted(arr.items(), key=lambda x: x[1])
tree_edges = 0
result = 0
step = []

while True:
    if tree_edges == N - 1:
        break
    point, weight = arr.pop(0)
    if find(point[0]) != find(point[1]):
        union(point[0], point[1])
        step.append((point[0], point[1]))
        result += weight
        tree_edges += 1

print(result)
