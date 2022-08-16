N = int(input())
arr = [''] * N
number_arr = []

# Left Padding
for i in range(N):
    line = list(input())
    temp = ['' for _ in range(10 - len(line))]
    temp.extend(line)
    arr[i] = temp

# 자릿수가 높은 알파벳부터 배열에 삽입
for i in range(10):
    for j in range(N):
        if arr[j][i] != '' and arr[j][i] not in number_arr:
            number_arr.append(arr[j][i])

# 자릿수가 높은 알파벳부터 큰 수 배정
num_dict = dict()
for i in range(len(number_arr)):
    num_dict[number_arr[i]] = 9 - i


# 알파벳을 상응하는 수로 컨버팅하여 계산
result = 0
for string in arr:
    temp = ''
    for i in range(len(string)):
        if string[i] != '':
            temp = temp + str(num_dict[string[i]])

    result += int(temp)

# 결과 출력
print(num_dict)
print(result)