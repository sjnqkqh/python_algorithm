n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [0] * (n + 1)
dp[0] = arr[0]
if n > 1: dp[1] = arr[0] + arr[1]

for i in range(2, n):
    dp[i] = max(dp[i - 1],  # 1,2번째 술을 마실 경우
                dp[i - 2] + arr[i],  # 1,3번째 술을 마실 경우
                dp[i - 3] + arr[i - 1] + arr[i])  # 2,3 번째 술을 마실 경우

print(max(dp))
