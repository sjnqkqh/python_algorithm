def solution(gems):
    answer = [0, len(gems)]
    goal_set = set(gems)
    a, b = 0, 0

    while a < len(gems) - 1 or b < len(gems) - 1:
        run_set = set(gems[a:b])
        if len(run_set) < len(goal_set) and b < len(gems):
            b += 1

        if len(run_set) == len(goal_set) and b - a < answer[1] - answer[0]:
            answer = [a, b]

        if len(run_set) == len(goal_set) or b == len(gems):
            a += 1

    answer = [answer[0]+1, answer[1]]

    return answer

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["XYZ", "XYZ", "XYZ"])
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
