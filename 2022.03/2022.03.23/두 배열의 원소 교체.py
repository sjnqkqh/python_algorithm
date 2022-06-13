# Page 182

n, k = map(int, input().split())

array_a = sorted(list(map(int, input().split())))
array_b = sorted(list(map(int, input().split())), reverse=True)

for i in range(k):
    if array_a[i] < array_b[i]:
        array_a[i], array_b[i] = array_b[i], array_a[i]
    else:
        break

print(sum(array_a))
