def solution(N, number):
    dp = [set() for _ in range(9)]
    dp[1] = {N}

    # N == number면 즉시 1 반환 및 종료
    if N == number:
        return 1

    # DP 시작
    for i in range(2, 9):
        # i를 구성하는 숫자쌍 간의 연산 결과를 dp에 삽입
        for j in range(1, (i // 2) + 1):
            pair_number = i - j
            for item1 in dp[pair_number]:
                for item2 in dp[i - pair_number]:
                    # dp 간의 연산 결과 삽입
                    dp[i].add(abs(item1 + item2))
                    dp[i].add(abs(item1 - item2))
                    dp[i].add(abs(item1 * item2))

                    if item2 != 0:
                        dp[i].add(abs(item1 // item2))

                    # i개로 이루어진 N의 연속을 삽입
                    dp[i].add(int(str(N) * i))

                    if (
                        abs(item1 + item2) == number
                        or abs(item1 - item2) == number
                        or abs(item1 * item2) == number
                        or (item2 != 0 and abs(item1 // item2) == number)
                        or int(str(N) * i) == number
                    ):
                        return i
    return -1


print(solution(5, 12))
print(solution(2, 11))
print(solution(1, 1))
