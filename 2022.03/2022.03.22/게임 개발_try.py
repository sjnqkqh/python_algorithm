# Page 118
import sys

n, m = map(int, input().split())

x, y, d = map(int, input().split())
result = 1
game_map = []

for i in range(n):
    game_map.append(list(map(int, sys.stdin.readline().split())))

while 1:
    # 방향 설정
    if d < 3:
        d = d + 1
    else:
        d = 0

    print("direction = ", d)

    # 이동
    if d == 0 and game_map[x][y + 1] != 0:
        y = y + 1
    elif d == 1 and game_map[x + 1][y] != 0:
        x = x + 1
    elif d == 2 and game_map[x][y - 1] != 0:
        y = y - 1
    elif d == 3 and game_map[x - 1][y] != 0:
        x = x - 1

    game_map[x][y] = 2
    result = result + 1

    if (
        game_map[x - 1][y] != 0
        and game_map[x + 1][y] != 0
        and game_map[x][y + 1] != 0
        and game_map[x][y - 1] != 0
    ):
        if d == 0:
            y = y + 1
        elif d == 1:
            x = x + 1
        elif d == 2:
            y = y - 1
        elif d == 3:
            y = y - 1

        if game_map[x][y] != 0:
            break
        else:
            result = result + 1

print("result=", result)
