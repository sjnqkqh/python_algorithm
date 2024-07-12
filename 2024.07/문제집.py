N, M = map(int, input().split())

front_link_dict = {}
rear_link_dict = {}
arr = []
for _ in range(M):
    arr.append(map(int, input().split()))

for i in range(N + 1):
    front_link_dict[i + 1] = i
    rear_link_dict[i] = i + 1

for a, b in arr:
    temp = front_link_dict[b]
    front_link_dict[b] = a
    rear_link_dict[a] = b
    rear_link_dict[temp] = a

idx, i = 0, 0
result = []


print(front_link_dict)
print(rear_link_dict)

## 우선순위 큐로 전환
while True:
    if i == N:
        break

    now = rear_link_dict[idx]
    i += 1
    idx = now
    result.append(now)

print(*result, sep=' ')
