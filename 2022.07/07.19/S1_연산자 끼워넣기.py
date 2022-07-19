from collections import deque

perm = []


def permutation(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        if len(chosen) == r:
            perm.append(chosen.copy())
            return

        for i in range(len(arr)):
            if not used[i] and (i == 0 or arr[i - 1] != arr[i] or used[i - 1]):
                chosen.append(arr[i])
                used[i] = True
                generate(chosen, used)
                used[i] = False
                chosen.pop()

    generate([], used)


def calculate(step: deque, arr: list):
    result = arr[0]
    for i in range(1, len(arr)):
        process = step.popleft()
        num = arr[i]

        if process == "+":
            result = result + num
        elif process == "-":
            result = result - num
        elif process == "/":
            if result < 0:
                result = ((result * -1) // num) * -1
            else:
                result = result // num
        else:
            result = result * num

    return result


N = int(input())
num_list = list(map(int, input().split()))
cnt_list = list(map(int, input().split()))

step = "+" * cnt_list[0] + "-" * cnt_list[1] + "*" * cnt_list[2] + "/" * cnt_list[3]

permutation(step, N - 1)
result_list = []
for p in perm:
    result_list.append(calculate(deque(p), num_list))

print(max(result_list))
print(min(result_list))
