# Page 226

# 화폐 종류의 수, 만들어야 하는 금액
n, m = map(int, input().split())

# 화폐의 종류
array = []
for i in range(n):
    array.append(int(input()))
array.sort()

# 모든 항에 INF 대입
d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:  # m을 만드는 방법이 존재할 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(m)
