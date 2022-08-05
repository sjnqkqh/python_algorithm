import string

tmp = string.digits + string.ascii_lowercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def is_prime_number(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    answer = 0
    converted = str(convert(n, k))
    num_list = []
    arr = converted.split('0')

    # 소수가 될 수 있는 수들 선별
    for item in arr:
        item.replace("0", "")
        if item != "":
            num_list.append(int(item))

    for item in num_list:
        if is_prime_number(item):
            answer += 1

    return answer