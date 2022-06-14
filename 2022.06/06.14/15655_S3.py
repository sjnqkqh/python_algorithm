# URL : https://www.acmicpc.net/problem/15655
import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))
permutations = list(itertools.permutations(arr, m))
permutations.sort()


def is_sorted(param):
    pre_number = 0
    for var in param:
        if pre_number > var:
            return False
        else:
            pre_number = var

    return True


for permutation in permutations:
    if is_sorted(permutation):
        for item in permutation:
            print(item, end=' ')
        print()

