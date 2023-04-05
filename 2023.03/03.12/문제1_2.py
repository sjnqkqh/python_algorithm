def solution(gems):
    n = len(gems)
    answer = [0, n]
    cnt = {gems[0]: 1}
    kind = len(set(gems))
    s, e = 0, 0

    while s < n and e < n:
        if len(cnt) < kind:
            e += 1
            if e == n:
                break
            cnt[gems[e]] = cnt.get(gems[e], 0) + 1
        else:
            if e - s < answer[1] - answer[0]:
                answer = [s + 1, e + 1]
            if cnt[gems[s]] == 1:
                del cnt[gems[s]]
            else:
                cnt[gems[s]] -= 1
            s += 1

    print(answer)

    return answer


solution([1, 2, 2, 3, 1, 2])
solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["XYZ", "XYZ", "XYZ"])
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
