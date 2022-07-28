N = int(input())


def check(arr):
    stack = []

    for item in arr:
        if item == ')':
            if len(stack) == 0:
                print("NO")
                return
            else:
                stack.pop()
        else:
            stack.append(item)

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")


for _ in range(N):
    arr = list(input())
    check(arr)
