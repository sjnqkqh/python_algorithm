# URL : https://www.acmicpc.net/problem/14501

n = int(input())

calendar = []
for i in range(1, n + 1):
    spending, gain = map(int, input().split())  # 소요일, 수입
    calendar.append({"day": i, "spending": spending, "gain": gain})

print(calendar)
