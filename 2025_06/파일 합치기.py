INF = 10 ** 9

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [[INF] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0

    sum_arr = [arr[0]]
    for i in range(1, n):
        sum_arr.append(sum_arr[i - 1] + arr[i])

    for k in range(1, n):
        for i in range(n):
            j = i + k
            if j < n:
                for pivot in range(i, j):
                    total_sum = 0
                    if i == 0:
                        total_sum = sum_arr[j]
                    else:
                        total_sum = sum_arr[j] - sum_arr[i - 1]
                    dp[i][j] = min(dp[i][j], dp[i][pivot] + dp[pivot + 1][j] + total_sum)

    print(dp[0][n-1])
