# 교재 118Page. 게임 개발 문제

n = 3
m = 3
load = [[1, 1, 1], [1, 0, 0], [1, 1, 0, 1]]

loc = dict()
loc['x'] = 1
loc['y'] = 1
loc['dir'] = 0

dx = [(1, 0), (0, 1), (-1, 0), (0, -1)]
result = 1
trigger = True


def turn():
    direction = loc['dir'] - 1
    if direction < 0:
        direction += 4
    loc['dir'] = direction


def road_check():
    direction = loc['dir'] - 1
    if direction < 0:
        direction += 4
    loc['dir'] = direction

    move = dx[loc['dir']]
    next_x = loc['x'] + move[0]
    next_y = loc['y'] + move[1]

    if 0 <= next_x < m and 0 <= next_y < n and load[next_y][next_x] == 0:
        return True

    return False


def move_character():
    load[loc['y']][loc['x']] = 1
    loc['x'] = loc['x'] + dx[loc['dir']][0]
    loc['y'] = loc['y'] + dx[loc['dir']][1]


check_count = 0
while trigger:

    if road_check():
        move_character()
        check_count = 0
        result += 1
        continue

    else:
        check_count += 1

    if check_count == 4:
        print(result)
        break
