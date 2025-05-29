import math
from collections import deque


def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    deq = deque()
    while x > 0:
        deq.appendleft(x % 10)
        x = x // 10

    while len(deq) > 1:
        pre, post = deq.popleft(), deq.pop()
        if pre != post:
            return False

    return True