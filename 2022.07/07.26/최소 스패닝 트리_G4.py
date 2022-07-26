N, M = map(int, input().split())
arr = []
parent = [0] * (N + 1)
link_count = 0
result = 0

# 그래프 입력
for _ in range(M):
    arr.append(list(map(int, input().split())))

# 간선 간의 가중치에 따른 그래프 정렬
arr = sorted(arr, key=lambda x: x[2])

# 부모 노드 초기화
for i in range(1, N + 1):
    parent[i] = i


# 부모 찾기 함수
def find_parent(num):
    if parent[num] != num:
        parent[num] = find_parent(parent[num])
    return parent[num]


# 합치기
def union(u, v):
    root_1 = find_parent(u)
    root_2 = find_parent(v)
    parent[root_2] = root_1


# 최소 신장 트리 구성
while True:
    if link_count == N - 1:
        break

    u, v, wt = arr.pop(0)
    if find_parent(u) != find_parent(v):
        union(u, v)  # 두 개의 간선을 하나의 집합으로 합친다 = 둘의 부모 노드를 통일한다.
        link_count += 1  # 간선의 갯수 증가
        result += wt  # 가중치 계산

print(result)
