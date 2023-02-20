T = int(input())
for _ in range(T):
    result = -1

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    gold = [[] for _ in range(n)]
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            gold[i].append(arr[(i * m) + j])

    for i in range(n):
        dp[i][0] = gold[i][0]

    for j in range(1, m):
        for i in range(n):
            cases = [dp[i][j - 1]]
            if i - 1 >= 0:
                cases.append(dp[i - 1][j - 1])
            if i + 1 < n:
                cases.append(dp[i + 1][j - 1])
            dp[i][j] = gold[i][j] + max(cases)

    for i in range(n):
        result = max(result, max(dp[i]))

    print(result)