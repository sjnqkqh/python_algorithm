import sys

input = sys.stdin.readline

n = int(input())
first = tuple(map(int, input().split()))
max1, max2, max3 = first
min1, min2, min3 = first

for _ in range(n - 1):
    now1, now2, now3 = tuple(map(int, input().split()))
    a = max(max1 + now1, max2 + now1)
    b = max(max1 + now2, max2 + now2, max3 + now2)
    c = max(max2 + now3, max3 + now3)
    max1, max2, max3 = a, b, c

    a = min(min1 + now1, min2 + now1)
    b = min(min1 + now2, min2 + now2, min3 + now2)
    c = min(min2 + now3, min3 + now3)

    min1, min2, min3 = a, b, c

print(max(max1, max2, max3), min(min1, min2, min3))
