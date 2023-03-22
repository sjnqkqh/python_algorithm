arr = []
for _ in range(9):
    arr.append(int(input()))
result_idx, result = -1, -1

for i in range(len(arr)):
    if arr[i] >= result:
        result_idx = i
        result = arr[i]

print(result)
print(result_idx+1)