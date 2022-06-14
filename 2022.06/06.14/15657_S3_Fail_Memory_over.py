# URL : https://www.acmicpc.net/problem/15657
import itertools
import sys

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()


# 리스트 내부의 모든 요소가 오름차순 정렬되어있는지 확인
def is_sorted(param):
    pre_number = 0
    for val in param:
        if pre_number > val:
            return False
        else:
            pre_number = val
    return True


# 종복을 포함하여 M개를 선택하는 모든 경우 생성
products = list(itertools.product(arr, repeat=m))
arr.clear()

for product in products:
    if is_sorted(product):
        for item in product:
            print(item, end=' ')
        print()