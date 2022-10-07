def solution(N, number):
    dp = [set() for _ in range(9)]

    dp[1] = {N}
    dp[2] = {N + N, N * N, N // N, 0, N * 11}

    for i in range(3, 9):
        # i 자리를 온전히 연속된 N으로 만드는 경우
        cycle = 1
        for j in range(1, i):
            cycle += 10 ** j
        dp[i].add(N * cycle)

        # dp[i-2]의 결과와 dp[i-1]의 결과를 사칙연산
        for item2 in dp[i - 2]:
            for item in dp[i - 1]:
                dp[i].add(item2 + item)
                dp[i].add(item2 - item)
                dp[i].add(item2 * item)

                if item != 0:
                    dp[i].add(item2 // item)

                if item2 + item == number or item2 - item == number or (item != 0 and item2 // item == number) or item2 * item == number or N * cycle == number:
                    return i - 1

    return -1


# print(solution(5, 12))
# print(solution(2, 11))
print(solution(4, 17))
# print(solution(5, 31168))
