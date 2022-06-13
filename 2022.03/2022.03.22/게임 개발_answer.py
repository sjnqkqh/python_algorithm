# N, M 입력
n, m = map(int, input().split())

# 현재 캐릭터의 좌표와 방향 입력
x, y, direction = map(int, input().split())

# 방문한 위치를 저장하기 위해 동일한 크기의 이차원 배열을 0으로 초기화
d = [[0] * m for _ in range(n)]
d[x][y] = 1

# 전체 맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 이동 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전 이후 움직임
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전 이후 이동이 불가할 때
    else:
        turn_time += 1

    # 네 방향 모두 이동이 불가할 때
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)

