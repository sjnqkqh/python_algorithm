from collections import deque

N = int(input())
K = int(input())

direction = ["U", "R", "D", "L"]
move_dict = {"U": [1, 0], "R": [0, 1], "D": [-1, 0], "L": [0, -1]}
move_arr = []  # 중간 동작 배열
arr = [[0] * N for _ in range(N)]  # 지도
now = 1

for _ in range(K):
    i, j = map(int, input().split())
    arr[N - i][j - 1] = 1

L = int(input())
for _ in range(L):
    line = input().split()
    move_arr.append([int(line[0]), line[1]])


def snake_game(move_queue: deque):
    global now
    time = 0
    snake = deque()
    snake.append([N - 1, 0])

    while True:
        time += 1
        move = move_dict.get(direction[now])

        i, j = snake[0]
        next_i = i + move[0]
        next_j = j + move[1]

        if (
            [next_i, next_j] in snake
            or 0 > next_i
            or next_i >= N
            or 0 > next_j
            or next_j >= N
        ):
            return time

        snake.appendleft([next_i, next_j])
        if arr[next_i][next_j] == 0:
            snake.pop()
        else:
            arr[next_i][next_j] = 0

        if move_queue and move_queue[0][0] == time:
            if move_queue[0][1] == "L":
                now = 3 if now == 0 else now - 1
            else:
                now = 0 if now == 3 else now + 1
            move_queue.popleft()


result = snake_game(deque(move_arr))
print(result)
