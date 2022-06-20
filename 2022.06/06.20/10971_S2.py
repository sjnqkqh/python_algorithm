# URL : https://www.acmicpc.net/problem/10971
import itertools

n = int(input())
arr = []
min_length = 1e9  #최소값 초기화

# 경로 입력
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 경로 순열 생성
permutation = itertools.permutations([i for i in range(n)])

# 순열을 순환하며 최단 경로 조회
for item in permutation:
    way_length = 0  # 한 바퀴 순환하는 거리
    way = list(item)
    now = 0  # 시작점 겸, 인덱스
    # 경로 순열 중 마지막 인수가 0 (복귀)인 경우
    if item[n - 1] == 0:
        able = True
        for i in way:
            # 경로가 끊긴 경우 해당 케이스 종료
            if arr[now][i] == 0:
                able = False
                break
            else:
                way_length = way_length + arr[now][i]
                now = i
        if able:
            min_length = min(min_length, way_length)
    else:
        continue

print(min_length)
