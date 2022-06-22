# URL : https://www.acmicpc.net/problem/14889
import itertools

n = int(input())
arr = []
stats = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

# 대각선 위치 선수와 스탯 합
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if i != j:
            stats.append(arr[j][i] + arr[i][j])

# 스탯 리스트 정렬
min_diff = 1e9  # 각 선수별 스탯 차의 최솟값
stats.sort()
print(stats)

print(min_diff)
