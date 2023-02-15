# Page 96

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    if result < min_value:
        result = min_value

print(result)
