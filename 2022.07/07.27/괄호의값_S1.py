arr = list(input())
stack = []
cal_result = 0
i = 0

# 정수로 변환 가능한 조합
while i < len(arr):
    if arr[i] == "(" and arr[i + 1] == ")":
        stack.append(2)
        i += 1

    elif arr[i] == "[" and arr[i + 1] == "]":
        stack.append(3)
        i += 1
    else:
        stack.append(arr[i])

    i += 1

print(*stack, sep=" ")


def get_minimum_string(stack: []):
    print(stack)
    str = ""
    start_idx = 0
    end_idx = 0

    for i in range(len(stack)):
        item = stack[i]
        if item == "(" or item == "[":
            str = item
            start_idx = i+1
        break

    for i in range(start_idx, len(stack)):
        item = stack[i]
        if (str == "(" and item == ")") or (str == "[" and item == "]"):
            end_idx = i
            break
    arr = stack[start_idx:end_idx]
    print(*arr, sep=" ")

    if "(" in arr or "[" in arr:
        get_minimum_string(arr)



get_minimum_string(stack)