import copy
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = 0
empty_block = {0: 0, 1: 0, 2: 0}
calc = [[copy.copy(empty_block) for _ in range(n)] for _ in range(n)]
calc[0][1] = {0: 1, 1: 0, 2: 0}

for i in range(n):
    for j in range(2, n):
        if arr[i][j] == 1:
            calc[i][j] = copy.copy(empty_block)

        else:
            post_block = empty_block if i < 1 else calc[i - 1][j - 1]
            post_up = empty_block if i == 0 else calc[i - 1][j]
            post_left = calc[i][j - 1]
            minus_block = empty_block if i < 2 else calc[i - 2][j - 2]

            if 0 < i and arr[i - 1][j] == 1:
                calc[i][j] = {
                    0: post_left[0] + post_left[1],
                    1: 0,
                    2: 0
                }
            elif arr[i][j-1] == 1:
                calc[i][j] = {
                    0: 0,
                    1: 0,
                    2: post_up[1] + post_up[2]
                }
            else:
                calc[i][j] = {
                    0: post_left[0] + post_left[1],
                    1: post_block[0] + post_block[1] + post_block[2],
                    2: post_up[1] + post_up[2]
                }

# for item in calc:
#     print(item)

print(calc[n-1][n-1][0]+ calc[n-1][n-1][1]+calc[n-1][n-1][2])