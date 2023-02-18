vector = [[0, -1], [1, 0], [0, 1], [-1, 0]]
result = 1
map_arr = []


def look_around(x: int, y: int):
    for i in range(4):
        next_x = x + vector[i][0]
        next_y = y + vector[i][1]

        if n > next_x >= 0 and m > next_y >= 0 and map_arr[next_x][next_y] == 0:
            return True

    return False


n, m = map(int, input().split(" "))
x, y, direction = map(int, input().split(" "))

for i in range(n):
    map_arr.append(list(map(int, input().split(" "))))

map_arr[x][y] = 1

while look_around(x, y):
    next_x = x + vector[direction][0]
    next_y = y + vector[direction][1]

    if next_x >= 0 and next_y >= 0 and map_arr[next_x][next_y] == 0:
        x, y = next_x, next_y
        map_arr[next_x][next_y] = 1
        result += 1
    else:
        if direction == 0:
            direction = 3
        else:
            direction -= 1

print(result)
