import itertools

n, m = map(int, input().split())
num_set = set(map(int, input().split()))
arr = [item for item in num_set]
arr.sort()

com = list(itertools.product(arr, repeat=m))
for item in com:
    pre = 0
    flag = True

    for i_item in item:
        if i_item < pre:
            flag = False
            break
        else:
            pre = i_item

    if flag:
        print(*item, sep=' ')
