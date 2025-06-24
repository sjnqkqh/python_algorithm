from collections import deque

st = deque(input())
boom = list(input())
stack = []
result_arr = []

while st:
    s = st.popleft()
    stack.append(s)
    if s == boom[-1]:
        is_boom = True
        for i in range(len(boom)):
            if len(stack) < len(boom) or stack[len(stack) - (len(boom) - i)] != boom[i]:
                is_boom = False
                break
        if is_boom:
            for _ in range(len(boom)):
                stack.pop()

result = ''
if not stack:
    result = 'FRULA'
else:
    result = ''.join(stack)

print(result)
