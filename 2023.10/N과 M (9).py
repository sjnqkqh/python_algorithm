n, m = map(int, input().split())
num_arr = list(map(int, input().split()))
num_arr.sort()

result_set = set()
for i in range(len(num_arr)):
    temp = [num_arr[i]]
    for idx in range(len(num_arr)):
        while idx < len(num_arr):
            if len(temp) == m:
                result_set.add(tuple(temp))
                temp.pop()
            elif i == idx:
                idx = idx + 1
            else:
                if idx < len(num_arr):
                    temp.append(num_arr[idx])
                idx = idx + 1

result = list(result_set)
result.sort()

for item in result:
    print(*item, sep=" ")


# def make_list(temp: list, temp_arr: list, limit: int):
#     if len(temp) == limit:
#         return temp
#     else:
#         temp.append(temp_arr.pop())
#         make_list(temp, temp_arr, limit)
