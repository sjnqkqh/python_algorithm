# Page 217

x = int(input())  # 정수값 X 입력

d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1

    # 인덱스가 5로 나누어 떨어지는 경우, 이전 수에서 1을 더한것 혹은 1/5 인덱스에서 1을 더한 것 중에 작은 것을 대입
    if i % 5 == 0:
        d[i] = min(d[i // 5] + 1, d[i])
    elif i % 3 == 0:
        d[i] = min(d[i // 3] + 1, d[i])
    elif i % 2 == 0:
        d[i] = min(d[i // 2] + 1, d[i])

print(d[x])
