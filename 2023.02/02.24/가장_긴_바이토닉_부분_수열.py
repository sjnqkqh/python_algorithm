import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
reverse_arr = arr[::-1]

increase = [1] * n
decrease = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if reverse_arr[i] > reverse_arr[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

decrease.reverse()
result = -1
for i in range(n):
    result = max(result, increase[i] + decrease[i] - 1)

print(result)
