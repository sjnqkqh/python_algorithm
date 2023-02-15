# URL : https://www.acmicpc.net/problem/6588
import bisect
import math
import sys

arr = []
while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break

    arr.append(num)


def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:  # i가 소수인 경우
            for j in range(i + i, n, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]


# 최댓값까지의 소수 목록을 생성 (에라토스테네스의 체)
maxNum = max(arr)
primeNumberList = prime_list(maxNum)

print(primeNumberList)

for num in arr:
    conjectureWrong = False
    for prime in primeNumberList:
        if num - prime in primeNumberList:
            x, y = prime, num - prime
            print("{} = {} + {}".format(x + y, x, y))
            break

    if conjectureWrong:
        print("Goldbach's conjecture is wrong.")
