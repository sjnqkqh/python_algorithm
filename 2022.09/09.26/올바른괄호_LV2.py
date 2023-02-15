def solution(s):
    stack = []
    for item in s:
        if item == "(":
            stack.append(item)
        elif stack != [] and stack[-1] == "(" and item == ")":
            stack.pop()
        else:
            return False

    return len(stack) == 0
