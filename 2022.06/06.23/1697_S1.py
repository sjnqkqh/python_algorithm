# URL : https://www.acmicpc.net/problem/1697

n, k = map(int, input().split())

result = 0
arr = [0 for _ in range(max(n, k) + max(n, k))]

if len(arr) < 3:
    arr = [0 for _ in range(3)]

for i in range(len(arr)):
    result += 1
    # 인덱스가 수빈이보다 앞에 있을 경우
    if i <= n:
        arr[i] = n - i

    # 인덱스가 수빈이보다 뒤에 있을 경우
    elif i > n:
        arr[i] = min(arr[i - 1] + 1, arr[i // 2] + 1) if i % 2 == 0 else arr[i - 1] + 1

# 소요 시간 정리 (arr[i+1]+ 1이 arr[i]보다 더 작은 경우)
for i in range(1, len(arr) - 1):
    arr[i] = (
        min(arr[i], arr[i + 1] + 1, arr[i // 2] + 1)
        if i % 2 == 0
        else min(arr[i], arr[i + 1] + 1)
    )
    arr[i] = (
        min(arr[i], arr[i - 1] + 1, arr[i // 2] + 1)
        if i % 2 == 0
        else min(arr[i], arr[i - 1] + 1)
    )

# 정답
ans = [arr[k + 1] + 1, arr[k]]
if k != 0:
    ans.append(arr[k - 1] + 1)

print(min(ans))
