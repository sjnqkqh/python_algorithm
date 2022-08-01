import itertools

N, K = map(int, input().split())
temp_arr = []
total_spell_set = set()
arr = []
result = 0

# 각 단어 내부의 중복 제거
for _ in range(N):
    temp = set(list(input()))
    temp_arr.append(sorted(list(temp)))

# 중복을 제거한 상태에서 길이가 K보다 긴 경우 버림 (어떤 경우에서도 불가능)
for item in temp_arr:
    if len(item) <= K:
        arr.append(item)

# 결과 배열들의 각 원소를 SET에 삽입 -> 중복 제거 이후 조합 생성
for item in arr:
    for spell in item:
        total_spell_set.add(spell)

total_spell_set = sorted(list(total_spell_set))

# 알파벳 조합 생성
combine = list(itertools.combinations(total_spell_set, K))

for spells in total_spell_set:  # 스펠링 조합
    temp_result = 0
    for word in arr:  # 단어 목록
        keep_search = True

        # 하나의 스펠링 조합이 몇개의 단어를 커버칠 수 있는지 확인
        for spell in word:
            if spell not in spells:
                # 하나라도 조합에 속하지 않으면 곧장 다음 단어로 넘어감
                keep_search = False
                break

        if keep_search:
            temp_result += 1

result = min(result, temp_result)

print(result)
