n = int(input())
n_is_minus = n < 0
n_abs = abs(n)
pre, ppre = 1, 0
now = 0
for i in range(n_abs - 1):
    now = pre + ppre
    now = now % 1000000000
    ppre = pre % 1000000000
    pre = now % 1000000000

if n == 0:
    print(0)
elif n_is_minus and n_abs % 2 == 0:
    print(-1)
else:
    print(1)

if n_abs == 1:
    print(1)
else:
    print(now)
