# Page 375

T = int(input())
n, m = map(int, input().split())
array = list(map(int, input().split()))

map = [[0 for i in range(n)] for j in range(m)]

# 지도 생성
for i in range(m):
    for j in range(n):
        map[i][j] = array[j * m + i]

way = 0;
direction = [-1, 0, 1]

for i in range(m - 1):
    # 0~2 중 way를 정해야 함
    for j in range(n):
        for k in range(3):
            if map[i][j]


## 30 Minutes over. I am quit