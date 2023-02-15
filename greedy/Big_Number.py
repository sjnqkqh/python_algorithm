#
# # n, m, k를 공백으로 나누어 입력 받음
# n, m ,k = map(int, input().split())
#
# # N개의 수를 공백으로 나누어 입력 받음
# data = list(map(int, input().split()))

n = 5
m = 7
k = 2

data = [3, 4, 3, 4, 3]

data.sort()

result = 0
count = 1
biggest_number = data[n - 1]
second_number = data[n - 2]

# 간단한 풀이, 하지만 M이 커지면 곤란함.
# for i in range(m):
#     if count > k:
#         result += second_number
#         count -= k
#     else:
#         result += biggest_number
#
#     count = count+1
#
# print(result)


# 수학적 풀이, 반복되는 수열을 구한 후 반복 횟수만큼 더함
repeat = []
repeat_count = m // (k + 1)
another_number_count = m % (k + 1)

# 반복되는 순열 구하기
for _ in range(k):
    repeat.append(biggest_number)
repeat.append(second_number)

# 반복되는 순열의 합을 더한 후, 반복횟수만큼 곱하기
# 이후, 나머지 덧셈 횟수만큼 순열의 요소 더하기
result = sum(repeat) * repeat_count
for i in range(another_number_count):
    result += repeat[i]

print(result)
