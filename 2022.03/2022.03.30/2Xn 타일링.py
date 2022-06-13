# URL : https://www.acmicpc.net/problem/11726
# 자격으로 푸는 거 실패했음.

n = int(input())

# n+1 길이의 정답 테이블 구성
d = [0 for i in range(n + 1)]

d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n]%10007)
