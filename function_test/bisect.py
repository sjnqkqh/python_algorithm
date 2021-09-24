from _bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    result = bisect_right(a, right_value) - bisect_left(a, left_value)
    return result

a = [1,2,3,3,3,3,4,4,8,9]


result1 = count_by_range(a, 4, 4)
result2 = count_by_range(a, -1, 3)

print(result1)
print(result2)
