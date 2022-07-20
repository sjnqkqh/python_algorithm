import math

# 숫자의 자릿수 N은 최대 8. 일반적인 소수 판별식으로는 약 1억개의 소수를 저장할 수 없음
N = int(input())
limit = 10 ** (N + 1)
arr = [1, 3, 7, 9]
start_arr = [2, 3, 5, 7]


# 소수 판별 함수
def is_mini_num(num):
    if num == 2:
        return True
    for i in range(2, num // 2):
        if num % i == 0:
            return False

    return True


# 소수를 만들 수 있는 수를 더해가며 소수 판별
def make_number(num):
    for item in arr:
        temp_num = (num * 10) + item

        # 새로 만든 수가 소수가 아니면 해당 작업 종료
        if not is_mini_num(temp_num):
            continue

        # 수의 자릿수가 최대치에 도달하지 못했다면, 한 자리 더하기
        if int(math.log10(temp_num)) < N - 1:
            make_number(temp_num)
        else:
            # 수의 자릿수가 최대치라면 출력
            print(temp_num)


# 자릿수가 1이면, 시작수 그대로 출력
if N == 1:
    for i in start_arr:
        print(i)
# 자릿수가 2 이상이면, 소수를 만들어 출력
else:
    for i in start_arr:
        make_number(i)
