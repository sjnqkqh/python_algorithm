import math
from collections import deque


def reverse(x: int) -> int:
    is_minus = x < 0
    result = 0
    x = abs(x)
    while x:
        x, mod = divmod(x, 10)
        result = result * 10 + mod

    result = result * -1 if is_minus else result

    if result > 2 ** 31 - 1 or result < -1 * (2 ** 31):
        result = 0

    return result


# print(reverse(8463847412))
print(reverse(-8463847412))
# print(reverse(7463847412))
# print(reverse(0))

# print(2**31)