# 해설을 참고한 결과 누적합 알고리즘을 적용해야 풀 수 있는 문제라고...


def solution(board, skills):
    answer = 0

    for skill in skills:
        effect = skill[-1] if skill[0] == 2 else skill[-1] * -1  # 스킬의 영향력
        for i in range(skill[1], skill[3] + 1):
            for j in range(skill[2], skill[4] + 1):
                board[i][j] += effect

    # Board를 순회하며, 남아있는 건물 카운팅
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1

    return answer


print(
    solution(
        [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
        [
            [1, 0, 0, 3, 4, 4],
            [1, 2, 0, 2, 3, 2],
            [2, 1, 0, 3, 1, 2],
            [1, 0, 1, 3, 3, 1],
        ],
    )
)
