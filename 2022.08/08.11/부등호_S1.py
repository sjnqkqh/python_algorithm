import itertools

K = int(input())
compare_arr = list(input().split())
number_arr = [i for i in range(0, 10)]

perm = itertools.permutations(number_arr, K + 1)
min_case, max_case = (int(1e9), int(1e9)), (0, 0)

for simulation in perm:
    keep_search = True
    for i in range(len(compare_arr)):
        if (compare_arr[i] == "<" and simulation[i] > simulation[i + 1]) or (
            compare_arr[i] == ">" and simulation[i] < simulation[i + 1]
        ):
            keep_search = False
            break

    if keep_search:
        min_case = min(min_case, simulation)
        max_case = max(max_case, simulation)

print(*max_case, sep="")
print(*min_case, sep="")
