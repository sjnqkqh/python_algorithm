# Page 115

loc = str(input())
result = 0

x = ord(loc[0]) - ord("a")
y = int(loc[1]) - 1

move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (-1, -2), (1, 2), (-1, 2)]

for i in move:
    if 0 <= (x + i[0]) < 8 and 0 <= (y + i[1]) < 8:
        result = result + 1

print(result)
