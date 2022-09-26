import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
M = int(input())
questions = [[] for _ in range(M)]
dictionary = dict()

for i in range(M):
    questions[i] = list(map(int, sys.stdin.readline().split()))


def make_dictionary():
    for i in range(1, N):
        for j in range(1, N):
            if i - j >= 0 and i + j - 1 < N and arr[i - j] == arr[i + j - 1]:
                dictionary[(i - j + 1, i + j)] = True
            else:
                break

    for i in range(1, N):
        for j in range(1, N):
            if i - j >= 0 and i + j < N and arr[i - j] == arr[i + j]:
                dictionary[(i - j + 1, i + j + 1)] = True
            else:
                break


make_dictionary()
for question in questions:
    S, E = question[0], question[1]
    if S == E or dictionary.get((S, E)):
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
