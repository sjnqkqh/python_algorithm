# 에라토네스의 체를 이용해 N자리 소수를 구한다.
# 이 중 0,2,4,5,6,8 (1,3,7,9 제외)가 포함된 소수는 목록에서 제외한다. (N이 1일 경우는 그냥 소수들 목록을 반환한다.)
# 오름차순으로 정렬하여 출력
import math

N = int(input())
limit = 10 ** N - 1  # 소수를 찾는 범위


# N이 2 이상인 경우
def get_mini_number():
    num_list = [True for _ in range(limit)]
    num_list[0], num_list[1] = False, False
    for i in range(2, int(limit ** (1 / 2))):
        for j in range(i + i, len(num_list), i):
            num_list[j] = False

    return num_list


def is_mini_number(number: int):
    for i in range(2, int(number ** (1 / 2))):
        if number % i == 0:
            return False

    return True


if N == 1:
    temp = [2, 3, 5, 7]
    for item in temp:
        print(item)
else:
    bool_list = get_mini_number()
    cnt = N - 1

    for i in range(10 ** (N - 1), len(bool_list)):
        keep_going = True
        if bool_list[i]:
            mini_number = i
            log10 = int(math.log10(mini_number))
            for j in range(1, log10 + 1):
                if not bool_list[mini_number // (10 ** j)]:
                    keep_going = False
                    break
            if not keep_going:
                continue

            print(i)