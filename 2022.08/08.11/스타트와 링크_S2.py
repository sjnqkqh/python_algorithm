N = int(input())
arr = []
person_arr = [i for i in range(N)]
result = int(1e9)
team_combine = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


# 팀 조합 설계
def set_team_combination(combine: list, m, level, idx):
    if level == m:
        team_combine.append(combine.copy())
        return

    for i in range(idx, len(person_arr)):
        combine.append(person_arr[i])
        set_team_combination(combine, N // 2, level + 1, i + 1)
        combine.pop()


# 팀 설계에 따른 각 팀간 점수차 계산
def calculate_team_score(team: list):
    another_team = person_arr.copy()
    for item in team:
        another_team.remove(item)

    start_team_score = 0
    for member in team:
        for other_member in team:
            start_team_score += arr[member][other_member]

    link_team_score = 0
    for member in another_team:
        for other_member in another_team:
            link_team_score += arr[member][other_member]

    return abs(start_team_score - link_team_score)


set_team_combination([], N // 2, 0, 0)  # 팀 조합 설정
for simulation_team in team_combine:  # 팀 조합을 순회하며, 가장 낮은 차이를 기록
    result = min(result, calculate_team_score(simulation_team))

print(result) # 정답 출력
