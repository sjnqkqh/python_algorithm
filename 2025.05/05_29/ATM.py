n = int(input())
arr = list(map(int, input().split()))
arr.sort()

pre_sum, now_sum, result =0,0,0

for item in arr:
    now_sum = pre_sum + item
    pre_sum = now_sum
    result += now_sum

print(result)