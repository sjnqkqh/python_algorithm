N, M, K = map(int, input().split(" "))
arr = sorted(list(map(int, input().split(" "))))

arr.sort(reverse=True)
max_number = arr[0]
smaller_number = arr[1]

result = 0
time = 0

for i in range(M):
    time += 1
    if time == K:
        result += smaller_number
        time = 0
    else:
        result += max_number

print(result)
