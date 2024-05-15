import itertools

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


def start(time, _seq, _score, order):
    plate = [False] * 4
    out = 0
    while out < 3:
        _seq = 0 if _seq == 9 else _seq
        if _seq == 3:
            roo = arr[time][0]
        elif _seq > 3:
            roo = arr[time][order[_seq - 1]]
        else:
            roo = arr[time][order[_seq]]

        if roo == 1:
            if plate[2]:
                plate[2] = False
                _score += 1

            if plate[1]:
                plate[1] = False
                plate[2] = True

            if plate[0]:
                plate[0] = False
                plate[1] = True
            plate[0] = True

        elif roo == 2:
            if plate[2]:
                plate[2] = False
                _score += 1

            if plate[1]:
                plate[1] = False
                _score += 1

            if plate[0]:
                plate[0] = False
                plate[2] = True

            plate[1] = True

        elif roo == 3:
            if plate[2]:
                plate[2] = False
                _score += 1

            if plate[1]:
                plate[1] = False
                _score += 1

            if plate[0]:
                plate[0] = False
                _score += 1

            plate[2] = True
        elif roo == 4:
            for i in range(3):
                if plate[i]:
                    plate[i] = False
                    _score += 1
            _score += 1
        else:
            out += 1

        _seq += 1

    return _seq, _score


result = 0
order_combines = list(itertools.permutations([i for i in range(1, 9)], 8))
for order in order_combines:
    order = list(order)

    seq, score = 0, 0
    for i in range(n):
        seq, score = start(i, seq, score, order)

    result = max(result, score)

print(result)
