n = int(input())

pre_no, pre_left, pre_right = 1, 1, 1
for i in range(n - 1):
    now_no = (pre_no + pre_left + pre_right) % 9901
    now_left = (pre_no + pre_right) % 9901
    now_right = (pre_no + pre_left) % 9901

    pre_no, pre_left, pre_right = now_no, now_left, now_right

print((pre_no + pre_left + pre_right) % 9901)

# 1 3
# 2 7
# 3 17
# 4 41
# 5 99
