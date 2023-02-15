# Page 220

n = int(input())
stored = list(map(int, input().split()))

sum = 0
i = 0
while i < n - 1:
    if i + 2 >= n - 1:  # 배열의 최대 길이를 초과하는 경우
        sum = sum + max(stored[i], stored[i + 1])
        break

    if stored[i] + stored[i + 2] < stored[i + 1]:
        sum = sum + stored[i + 1]
        print("index: ", i + 1, end=" ")

    else:
        sum = sum + stored[i + 2]
        print("index: ", i + 2, end=" ")

    i = i + 2

    print("sum: ", sum)

print(sum)
