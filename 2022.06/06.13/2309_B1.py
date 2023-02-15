# URL : https://www.acmicpc.net/problem/2309

import sys

arr = []
finished = False

for _ in range(0, 9):
    arr.append(int(sys.stdin.readline()))

for i in range(0, 9):
    for j in range(0, 9):
        if i == j:
            continue

        # 두 난쟁이를 뺀 합 구하기
        smalls = arr.copy()
        smalls.remove(arr[i])
        smalls.remove(arr[j])
        sumLength = sum(smalls)

        if sumLength == 100:
            finished = True
            smalls.sort()
            for length in smalls:
                print(length)
            break
    if finished:
        break
