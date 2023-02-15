N = int(input())
# start = 10 ** (N - 1)
# end = 10 ** N
# result = 0
#
# for i in range(start, end):
#     num_arr = list(map(int, str(i)))
#     is_stair = True
#     for i in range(1, len(num_arr)):
#         stair_small, stair_big = num_arr[i] - 1, num_arr[i] + 1
#
#         if num_arr[i - 1] != stair_big and num_arr[i - 1] != stair_small:
#             is_stair = False
#             break
#
#     if is_stair:
#         result += 1
#
# print(result)
dp = [0] * (N + 1)
dp[1] = 9

for i in range(2, N + 1):
    dp[i] = (dp[i - 1] * 2) - (i - 1)

print(dp[-1] // 1000000000)
