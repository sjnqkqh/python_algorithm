import math


def recursive_minus(arr: list, val):
    big_num = int(math.log(val, 2))
    val -= int(math.pow(2, big_num))
    arr.append(big_num)

    if val == 0:
        return arr
    else:
        return recursive_minus(arr, val)


a, b, c = map(int, input().split())
if a == c:
    print(0)
else:
    dict = {0: a % c}
    result = recursive_minus([], b)
    for i in range(1, result[0] + 1):
        dict[i] = (dict[i - 1] * dict[i - 1]) % c

    answer = dict[result[0]]
    for i in range(1, len(result)):
        answer = (answer * dict[result[i]]) % c

    print(answer)
