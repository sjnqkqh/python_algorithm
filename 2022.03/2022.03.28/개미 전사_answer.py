# Page 222

# 전형적인 DP 문제

# 정수 n을 입력
n = int(input())

# 모든 배열 입력 받기
array = list(map(int, input().split()))

# 앞선 결과를 저장할 DP 테이블
d = [0] * 100

# solve
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 2] + array[i], array[i - 1])

print(d[n - 1])
