T = int(input())
for _ in range(T):
    n = int(input())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    elif n == 2:
        print(1, 1)
    else:
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        print(dp[-3], dp[-2])
