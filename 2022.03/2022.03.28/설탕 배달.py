# URL : https://www.acmicpc.net/problem/2839
# 해당 문제의 경우, 226 Page 효율적인 화폐 구성과 동일한 구조이다. 화이팅

n = int(input())
vals = [3, 5]

INF = 5001
d = [INF for i in range(n + 1)]

# 가장 작은 수의 배수부터 만들 수 있는 각 항 별로 만드는데 들어가는 포대의 수를 구한다.
d[0] = 0

for val in vals:
    for i in range(val, n + 1):
        # print(i * val, end=' ')
        # d[i * val] = min(i, d[i - val] + 1)
        if d[i - val] != INF:
            d[i] = min(d[i], d[i - val] + 1)

if d[n] != INF:
    print(d[n])
else:
    print(-1)
