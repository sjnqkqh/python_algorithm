import math

INF = int(1e9)


def solution(N, number):
    answer = 0
    dp = [INF] * (number + N)
    length = len(dp)
    dp[1] = 1 if N == 1 else 2

    # N의 곱으로 표현되는 노드 i에 대해 i/N으로 정의
    for i in range(1, (length // N) + 1):
        if i * N < length:
            dp[i * N] = min(dp[i * N], i)

    # N과 11, 111...의 곱으로 표현되는 i에 대해 정의

    multiple = 1
    for j in range(2, int(math.log10(number)) + 2):
        multiple = (multiple * 10) + 1
        for i in range(multiple, multiple * 9, multiple):
            if i < length:
                dp[i] = min(dp[i], int(math.log10(i)) + 2)

    # N의 제곱수로 표현되는 i에 대해 N 제곱근으로 정의
    multiple = 2
    while True:
        if N**multiple <= length:
            dp[N**multiple] = min(dp[N**multiple], multiple)
            multiple += 1
        else:
            break

    for i in range(2, length):
        num_arr = [dp[i]]  # 기존 수

        # dp[i의 약수] * 약수

        if 0 <= i - N < length:
            num_arr.append(dp[i - N] + 1)

        if 0 <= i - 1 < length:
            num_arr.append(dp[i - 1] + 2)

        if 11 < i < length:
            num_arr.append(dp[i - 1] + 1)

        dp[i] = min(num_arr)

    # 역행하면서 다음 노드가 현 노드보다 2 이상 크다면 교체
    for i in range(length - 2, 1, -1):
        dp[i] = min(dp[i], dp[i + 1] + 2)

    return dp[number] if dp[number] <= 8 else -1


print(solution(5, 31168))
