n, r, c = map(int, input().split())


def get_quarter(i, j, min_num: int, max_num: int, length):
    if length == 1:
        return min_num
    if i < length // 2 and j < length // 2:
        i = i
        j = j
        new_min_num = min_num
        new_max_num = (min_num + ((max_num + 1 - min_num) // 4)) - 1
        length = length // 2
        return get_quarter(i, j, new_min_num, new_max_num, length)

    elif i >= length // 2 and j < length // 2:
        i = i - length // 2
        j = j
        new_min_num = min_num + ((max_num + 1 - min_num) // 4)
        new_max_num = (min_num + ((max_num + 1 - min_num) // 4)*2) - 1
        length = length // 2
        return get_quarter(i, j, new_min_num, new_max_num, length)

    elif i < length // 2 and j >= length // 2:
        i = i
        j = j - length // 2
        new_min_num = min_num + ((max_num + 1 - min_num) // 4) * 2
        new_max_num = (min_num + ((max_num + 1 - min_num) // 4) * 3) - 1
        length = length // 2
        return get_quarter(i, j, new_min_num, new_max_num, length)

    else:
        i = i - length // 2
        j = j - length // 2
        min_num = min_num + ((max_num + 1 - min_num) // 4) * 3
        max_num = (min_num + ((max_num + 1 - min_num) // 4) * 4) - 1
        length = length // 2
        return get_quarter(i, j, min_num, max_num, length)


result = get_quarter(c, r, 0, 2 ** (n * 2) - 1, 2 ** n)
print(result)
