from collections import deque

MOVE = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def solution(board, r, c):
    answer = 0
    return answer


def bfs(board, visited, i, j):
    queue = deque()
    queue.append([i, j])
    board_size = len(board[0])
    turn = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            i, j = queue.popleft()
            move = get_move(board, visited, i, j)

            for item in MOVE:
                move.append([i + item[0], j + item[1]])

            for item in move:
                next_i = item[0]
                next_j = item[1]

                if 0 <= next_i < 4 and 0 <= next_j < 4 and not visited[next_i][next_j]:
                    queue.append([next_i, next_j])
                    visited[next_i][next_j] = False

        turn += 1


def get_move(board, visited, now_i, now_j):
    result = []
    board_size = len(board)
    for i in range(now_i, -1, -1):
        if board[i][now_j] != 0 or i == 0:
            if visited[i][now_j]:
                break
            else:
                result.append([i, now_j])

    for i in range(now_i, board_size):
        if board[i][now_j] != 0 or i == board_size - 1:
            if visited[i][now_j]:
                break
            else:
                result.append([i, now_j])

    for j in range(now_j, -1, -1):
        if board[now_i][j] != 0 or j == 0:
            if visited[now_i][j]:
                break
            else:
                result.append([now_i, j])

    for j in range(now_j, board_size):
        if board[now_i][j] != 0 or j == board_size - 1:
            if visited[now_i][j]:
                break
            else:
                result.append([now_i, j])

    return result
