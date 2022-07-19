import math

N, M, R = map(int, input().split())

arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))


# 2차원 배열 내부의 사각형의 테두리의 길이를 통해 최대 반복 횟수 도출
def get_cycle():
    square_list = []
    n, m = N, M
    lcm = 1
    while min(n, m) >= 1:
        square_list.append((n * 2) + (m * 2) - 4)  # 사각형의 둘레
        n = n - 2
        m = m - 2

        for i in range(len(square_list)):
            gcd = math.gcd(lcm, square_list[i])
            lcm = lcm * square_list[i] // gcd

    return lcm


# x1: 최소 x 값 index, x2: x값 최대 index
# y1: 최소 y 값 index, y2: y값 최대 index
def turn(arr: [[]], x1, x2, y1, y2):
    cover_point = [arr[y2][x1], arr[y1][x2]]
    print(cover_point)
    for i in range(y1, y2):
        arr[y2 - i][x1] = arr[y2 - i - 1][x1]
        arr[i][x2] = arr[i + 1][x2]

    for i in range(x1, x2):
        arr[y2][x2 - i] = arr[y2][x2 - i - 1]
        arr[y1][i] = arr[y1][i + 1]

    arr[y2][x1 + 1] = cover_point[0]
    arr[y1][x2 - 1] = cover_point[1]

    return arr


max_cycle_time = get_cycle()  # 최대 반복 횟수 -> 이만큼 순환하면 무조건 처음과 동일한 상태의 배열로 돌아옴
arr = turn(arr, 0, M - 1, 0, N - 1)
for item in arr:
    print(item)

print()

arr = turn(arr, 1, M - 2, 1, N - 2)
for item in arr:
    print(item)
