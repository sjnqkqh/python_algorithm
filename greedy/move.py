# input
# n = int(input())
# course = input().split()

n = 5
course = ["R", "R", "R", "U", "D", "D"]

loc = dict()
loc["x"] = 1
loc["y"] = 1


for move in course:
    if move == "L":
        if loc["y"] == 1:
            continue
        else:
            loc["y"] = loc["y"] - 1

    if move == "R":
        if loc["y"] == n:
            continue
        else:
            loc["y"] = loc["y"] + 1

    if move == "U":
        if loc["x"] == 1:
            continue
        else:
            loc["x"] = loc["x"] - 1
    if move == "D":
        if loc["x"] == n:
            continue
        else:
            loc["x"] = loc["x"] + 1
    print(loc)

print(loc["x"], loc["y"])
