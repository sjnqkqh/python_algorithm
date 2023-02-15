# input
# n, m = map(int, input().split())

n = 30
k = 5
cal_count = 0

while n != 1:
    if n % k == 0:
        n = n / k
    else:
        n = n - 1
    cal_count += 1

print(cal_count)
