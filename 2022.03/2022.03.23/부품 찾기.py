# Page 197

# 총 가게 부품 목록 입력
n = int(input())
stored = list(map(int, input().split()))

# 주문 받은 부품 목록 입력
m = int(input())
requests = list(map(int, input().split()))

# 상품 배열 정렬
stored.sort()


# 이진 탐색 함수 구현
def binary_search(array, target, start, end):
    if start > end:
        return None

    # 중간값 계산
    mid = (start + end) // 2

    # 이진탐색
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for request in requests:
    result = binary_search(stored, request, 0, n - 1)
    if result is None:
        print("no")
    else:
        search_start = result
        print("yes")
