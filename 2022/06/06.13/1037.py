# URL : https://www.acmicpc.net/problem/1037

n = int(input())  # 약수의 개수
arr = list(map(int, input().split()))  # 진짜 약수들
arr.sort()

print(min(arr) * max(arr))
