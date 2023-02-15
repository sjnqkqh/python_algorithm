# Page 201

n, m = map(int, input().split())  # 떡의 갯수와 손님이 요청한 떡의 길이
array = list(map(int, input().split()))  # 떡의 개별 높이
cut_list = []


# array의 모든 노드에 기존 노드의 수치를 초과하지 않도록 일정 수치만큼 차감했을 때, 배열의 합이 m이상이 나오도록
# 결국 sum(array) > m 가 성립하는 최대치를 구하라. 시작치는 0, 종료치는 max(array)


def cutting(array, start, end):
    if start > end:
        return None

    # 중간값
    mid = (start + end) // 2

    # 중간값만큼 각 노드에서 마이너스
    cut = []
    for i in range(n):
        length = array[i]
        cut.append(length - min(mid, length))

    if sum(cut) >= m:
        cut_list.append(mid)
        return cutting(array, mid + 1, end)
    else:
        return cutting(array, start, mid - 1)


cutting(array, 0, max(array))
print(max(cut_list))
