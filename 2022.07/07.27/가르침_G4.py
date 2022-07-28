N, K = map(int, input().split())
temp_arr = []
arr = []

for _ in range(N):
    temp = set(list(input()))
    temp_arr.append(sorted(list(temp)))

for item in temp_arr:
    if len(item) <= K:
        arr.append(item)

print(arr)



