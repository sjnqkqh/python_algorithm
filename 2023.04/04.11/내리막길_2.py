move_arr = [[1, 0], [0, 1], [-1, 0], [0, -1]]
n, m = map(int, input().split())
arr = []
dp = [[0] * m for _ in range(n)]
dp[n - 1][m - 1] = 1
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        # if i == n - 1 and j == m - 1:
        #     pass

        for move in move_arr:
            ni, nj = i + move[0], j + move[1]
            if n > ni > -1 and m > nj > -1 and arr[i][j] > arr[ni][nj]:
                dp[i][j] += dp[ni][nj]

for d in dp:
    print(d)