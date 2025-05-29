import math

n = int(input())


def solution(n):
    result = n
    while True:
        log_cnt = int(math.log(result, 10))
        if log_cnt % 2 == 0:
            result = int(math.pow(10, log_cnt+1))
            continue

        num_arr = str(result)
        pre = num_arr[:int(len(num_arr) / 2)]
        post = num_arr[int(len(num_arr) / 2):]

        calc_1, calc_2 = pre[0], post[0]
        for i in range(1, len(pre)):
            item = pre[i]
            calc_1 = int(calc_1) * int(item)

        for i in range(1, len(post)):
            item = post[i]
            calc_2 = int(calc_2) * int(item)

        if calc_1 == calc_2:
            return result
        else:
            result += 1