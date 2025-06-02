import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))
dp = [0] * (k + 1)
dp[0] = 1

coins = []
for _ in range(n):
    coin = int(input())
    if coin <= 10000:
        coins.append(coin)

for coin in coins:
    for i in range(1, k + 1):
        if i>=coin and dp[i-coin] != 0:
            dp[i] += dp[i-coin]

print(dp[k])
