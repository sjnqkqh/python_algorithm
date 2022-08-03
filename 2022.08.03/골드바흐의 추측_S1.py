arr = []
while True:
    num = int(input())
    if num == 0:
        break
    arr.append(num)


def is_prime_number(n: int):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def check(n: int):
    for i in range(1, (n // 2)+1):
        if is_prime_number(i) and is_prime_number(n - i):
            return [n, i, n - i]


for item in arr:
    result = check(item)
    print('{} = {} + {}'.format(result[0], result[1], result[2]))
