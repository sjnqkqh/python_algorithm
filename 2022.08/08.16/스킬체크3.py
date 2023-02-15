def solution(sticker):
    answer = 0

    dp = [[False, []]] * len(sticker)  # dp[i][0]은 i 번째까지의 합, dp[i][1]은 i번째까지의 배열
    dp[0] = [sticker[0], [0]]
    if len(sticker) > 1:
        dp[1] = [sticker[1], [1]]

    for i in range(2, len(sticker)):
        if dp[i - 2][0] + sticker[i] > dp[i - 1][0] - sticker[i - 1] + (
            sticker[i + 1] if i < len(sticker) - 1 else 0
        ):
            arr: list = dp[i - 2][1].copy()
            arr.append(i)
            dp[i] = [dp[i - 2][0] + sticker[i], arr]
        else:
            dp[i] = [dp[i - 1][0] - sticker[i - 1], dp[i - 1][1]]

    for item in dp:
        answer = max(answer, item[0])

    print(dp)

    return answer


solution([14, 6, 5, 110, 3, 9, 2, 100])
solution([14, 6, 5, 11, 3, 9, 2, 10])
solution([1, 3, 2, 5, 4])
