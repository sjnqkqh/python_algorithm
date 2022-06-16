# URL : https://www.acmicpc.net/problem/11053

n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = 1


# 입력한 길이만큼 이전 배열이 지속적으로 증가하였는지 확인
def is_increasing(array: list, idx: int, length: int):
    for j in range(idx - length, idx):
        if array[j] >= array[idx]:
            return False

    return True


for i in range(1, n):
    if is_increasing(arr, i, dp[i - 1]):
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i - 1]

print(dp[n - 1])
