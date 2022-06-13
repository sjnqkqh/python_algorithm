n = int(input())
p = 0
if n % 5 == 0:
    print(n // 5)
else:
    while n > 0:
        n -= 3
        p += 1
        if n % 5 == 0:
            print(p + (n // 5))
            break
        elif n == 1 or n == 2:
            print(-1)
            break
        elif n == 0:
            print(p)
            break
