# Page 169.
# 기존 코드보다 약간 성능이 저하되지만 심플한 코드

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗은 제외한 나머지 원소

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(array))

array = [('바나나', 2), ('사과', 5), ('당근', 3)]
def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)
