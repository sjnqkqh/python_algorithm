N, K = map(int, input().split())
arr = []
target_spells = set()
combine = [0 for _ in range(K)]
result = 0

# 비트마스킹 처리
for _ in range(N):
    temp = set(list(input()))
    spell_check = 0b0

    for spell in temp:
        spell_check = spell_check | (1 << (ord(spell) - ord('a')))
        target_spells.add(ord(spell) - ord('a'))

    arr.append(spell_check)

target_spells = list(target_spells)


# 조합 생성 및 비트 비교
def get_combination(N, M, level, idx):
    global result

    # list To Bit_mask
    if level == M:
        case_result = 0
        compare_bit = 0b0

        for item in combine:
            compare_bit = compare_bit | (1 << item)

        for spell_bit in arr:
            if spell_bit & compare_bit == spell_bit:
                case_result += 1

        result = max(result, case_result)
        return

    for i in range(idx, N):
        combine[level] = target_spells[i]
        get_combination(N, M, level + 1, i + 1)


if len(target_spells) < K:
    print(N)
else:
    get_combination(len(target_spells), K, 0, 0)
    print(result)
