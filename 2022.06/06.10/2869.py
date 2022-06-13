a, b, c = map(int, input().split())

rest = (c - a) % (a - b)
result = (c - a) // (a - b)
if rest == 0:
    result = result + 1
else:
    result = result + 2

print(result)
