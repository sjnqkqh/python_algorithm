n = "a2"

x = ord(list(n)[0]) - ord("a") + 1
y = int(list(n)[1])
result = 0

step = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2)]

for move in step:
    next_x = x + move[0]
    next_y = y + move[1]

    if 1 <= next_x <= 8 and 1 <= next_y <= 8:
        result += 1

print(result)
