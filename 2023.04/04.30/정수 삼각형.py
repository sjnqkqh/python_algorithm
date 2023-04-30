arr = []
n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(arr[i])):
        d = []
        if j != 0:
            d.append(arr[i - 1][j - 1] + arr[i][j])
        if j != len(arr[i]) - 1:
            d.append(arr[i - 1][j] + arr[i][j])
        arr[i][j] = max(d)

print(max(arr[-1]))
