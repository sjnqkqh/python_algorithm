# URL : https://www.acmicpc.net/problem/1978

# 소수 찾기

n = int(input())  # 입력될 수의 개수 (100 이하)
arr = list(map(int, input().split()))  # 소수인지 판별할 수
result = 0

for num in arr:
    for i in range(2, num+1):  # 소수는 1과 자신 외의 수로 나누어 떨어지지 않는 수
        if i == num:  # num이 소수일 경우
            result = result + 1

        if num % i == 0:
            break

print(result)
