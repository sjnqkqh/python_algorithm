# Page 168


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return

    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1  # 피벗의 다음 원소부터
    right = end  # 입력받은 마지막 원소까지

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 왼쪽에서 출발한 탐색(피벗보다 큰 데이터를 찾는 탐색)과 오른쪽에서 출발한 탐색(피벗보다 작은 데이터를 찾는 탐색)이 엇갈리면,
        # 피벗과 작은 수 (array[right])를 교체한다.
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array) - 1)
print(array)
