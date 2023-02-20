n = int(input())
dp = [0] * (30)
max_value = 0
schedule_list = []

for _ in range(n):
    a, b = map(int, input().split())
    schedule_list.append((a, b))

for i in range(n - 1, -1, -1):
    time, pay = schedule_list[i]
    point = i + time
    if point <= n:
        dp[i] = max(max_value, dp[point] + pay)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(dp)
print(max(dp[:n + 1]))
