from collections import deque

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
questions = []
dictionary = dict()

for _ in range(M):
    questions.append(list(map(int, input().split())))


def make_dictionary():
    for i in range(1, N):
        for j in range(1, N):
            if i - j >= 0 and i + j - 1 < N and arr[i - j] == arr[i + j - 1]:
                dictionary[(i, i + 1)] = True
            else:
                break

    for i in range(1, N):
        for j in range(1, N):
            if i - j >= 0 and i + j < N and arr[i - j] == arr[i + j]:
                dictionary[(i - j + 1, i + j + 1)] = True
            else:
                break


make_dictionary()
print(dictionary)
for question in questions:
    S, E = question[0], question[1]
    if S == E or dictionary.get((S, E)):
        print(1)
    else:
        print(0)
