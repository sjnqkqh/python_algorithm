# 문제 설명 너무 못 썼다... 이과생 같으니라고
# 입력 받기
n = 2
m = 4
min_num = 0
number_list = ([7, 3, 1, 8], [3, 3, 3, 4])

for i in range(n):
    data = number_list[i]

    if min_num < min(data):
        min_num = min(data)

print(min_num)
