set = set([1, 2, 3, 4, 5, 6])

if "not in" not in set:
    set.add("not in")

print(set)

a = [1, 2, 4, 5, 5, 5, 3, 4, 5]
remove_set = {3, 5}

result = [num for num in set if num not in remove_set]

print(result)
