N, M = map(int, input().split())
name_dict = dict()
name_list = []
result = 0

for _ in range(N):
    name_dict[input()] = True

for _ in range(M):
    name = input()

    if name_dict.get(name):
        result += 1
        name_list.append(name)

print(result)
for item in sorted(name_list):
    print(item)
