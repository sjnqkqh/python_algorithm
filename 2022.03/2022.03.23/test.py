from collections import deque

a = deque((1, 2))
b = deque()
b.append((1, 2))

print(a)
print(b)

q= a[1]
e, r = b.popleft()

print(q)
print(e, r)
