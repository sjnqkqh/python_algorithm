# URL : https://www.acmicpc.net/problem/15650
import itertools

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]

permutations = itertools.permutations(arr, m)

for permutation in permutations:
    answer = []
    preNum = 0

    for i in permutation:
        if i < preNum:
            answer = []
            break
        else:
            preNum = i
            answer.append(i)

    for num in answer:
        print(num, end=" ")
    if len(answer):
        print()
