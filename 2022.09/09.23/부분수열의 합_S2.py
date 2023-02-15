N, S = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(len(arr) + 1):
    for j in range(len(arr) + 1):
        if arr[j:i] != [] and sum(arr[j:i]) == S:
            result += 1

print(result)
