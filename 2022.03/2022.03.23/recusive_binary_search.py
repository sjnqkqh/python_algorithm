# Page 189

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid

    # 중간점보다 찾는 값이 더 작다면 배열의 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    # 중간점보다 찾는 값이 더 크다면 배열의 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)


# n(원소의 갯수)와 대상 입력
n, target = map(int, input().split())

# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진탐색 수행 결과
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
