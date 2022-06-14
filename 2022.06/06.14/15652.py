# URL : https://www.acmicpc.net/problem/15652
import itertools

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]

result = itertools.product(arr, repeat=m)

for item in result:
    answers = []
    preNum = 0
    for i in item:
        if preNum <= i:
            answers.append(i)
            preNum = i
        else:
            answers.clear()
            break

    if len(answers):
        for answer in answers:
            print(answer, end=' ')
        print()
