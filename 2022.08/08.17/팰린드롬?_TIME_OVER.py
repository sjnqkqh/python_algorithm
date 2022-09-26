from collections import deque

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
questions = []
dictionary = dict()

for _ in range(M):
    questions.append(list(map(int, input().split())))


def make_dictionary():
    for i in range(2, 4):
        queue = deque()

        for j in range(N):
            queue.append(arr[j])
            if len(queue) > i:
                queue.popleft()

            if len(queue) == i and is_felindrom(queue):
                dictionary[j - i + 2, j + 1] = True


def is_felindrom(origin_queue: deque):
    queue = origin_queue.copy()

    while len(queue) > 1:
        a = queue.popleft()
        b = queue.pop()

        if a != b:
            return False

    return True


make_dictionary()

for question in questions:
    S, E = question[0], question[1]
    if S == E or dictionary.get((S, E)) is not None:
        print(1)
    else:
        print(0)
