# Page 180

n = int(input())

array = [[] for i in range(101)]

for _ in range(n):
    name, score = input().split()
    array[int(score)].append(name)

# print(array)

for arr in array:
    while arr:
        print(arr.pop(), end=' ')