N = int(input())
arr = list(map(int, input().split()))
num_dict = dict()
result = 0

if N % 2 == 0:
    pre_list = arr[: N // 2]
    post_list = arr[N // 2 :]
else:
    pre_list = arr[: N // 2]
    post_list = arr[(N // 2) + 1 :]

post_list.reverse()
print(pre_list)
print(post_list)
LCS = [[0] * (len(pre_list) + 1) for _ in range(len(pre_list) + 1)]


for i in range(0, len(post_list)):
    for j in range(0, len(post_list)):
        print(i, j)
        if pre_list[i] == post_list[i]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

for item in LCS:
    print(item)
