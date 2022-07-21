from collections import deque

N, M = map(int, input().split())
arr = list(map(int, input().split()))
post_list = deque()
result = 0

for i in range(M):
    if (i == 0 or arr[i - 1] < arr[i]) and (i == M - 1 or arr[i + 1] <= arr[i]):
        post_list.append(i)

# 시작점 - post 중간 높이와 min(start, post)간의 차이를 result에 저장
# post가 arr의 마지막 요소가 아니라면 다음 post를 post_list에서 찾는다. 만약 다음 post가 없다면 시뮬레이션을 종료한다.

start = -1  # 빗물이 고이기 시작할 INDEX
pivot = 0
while post_list:
    skip = False
    post = post_list.popleft()

    # 빗물이 고이기 시작할 인덱스 탐색 (시작점부터 포스트까지 다음 인덱스보다 높이가 높은 지점 탐색)
    for i in range(pivot, post):
        if arr[i] > arr[i + 1]:
            start = i
            break

    # 빗물이 고이기 시작할 인덱스가 정해지지 않았다면 (포스트까지 높이가 똑같거나 높아지기만 하는 경우), 이번 포스트는 패스
    if start == -1:
        skip = True

    # 만약 현재 쌓을 수 있는 빗물의 높이보다 다음 포스트를 이용해서 쌓을 수 있는 수면의 높이가 높다면
    # 이 포스트로 빗물을 쌓는건 패스한다.
    rain_height = min(arr[start], arr[post])
    for i in range(post, M):
        if min(arr[start], arr[i]) > rain_height:
            rain_height = min(arr[start], arr[i])
            post = i
            skip = True

    # 수면의 높이에서 기둥의 높이를 뺀 값을 빗물의 양 결과값에 더한다.
    # 이 때, 포스트의 높이가 수면보다 높은 경우는 0으로 처리한다.
    if not skip:
        for item in range(start + 1, post):
            result += rain_height - arr[item] if rain_height - arr[item] > 0 else 0

        pivot = post

print(result)
