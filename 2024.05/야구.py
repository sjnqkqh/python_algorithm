import itertools
import sys

input = sys.stdin.readline

result = 0
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


for order in itertools.permutations(range(1, 9), 8):
    seq, score = 0, 0
    for i in range(n):
        plate = [False] * 3
        out = 0
        while out < 3:
            seq = 0 if seq == 9 else seq
            if seq == 3:
                roo = arr[i][0]
            elif seq > 3:
                roo = arr[i][order[seq - 1]]
            else:
                roo = arr[i][order[seq]]

            if roo == 1:
                if plate[2]:
                    score += 1
                plate = [True, plate[0], plate[1]]
            elif roo == 2:
                score += plate[2] + plate[1]
                plate = [False, True, plate[0]]
            elif roo == 3:
                score += plate[0] + plate[1] + plate[2]
                plate = [False, False, True]
            elif roo == 4:
                score += plate[0] + plate[1] + plate[2] + 1
                plate = [False, False, False]
            else:
                out += 1

            seq += 1
    result = max(result, score)

print(result)
