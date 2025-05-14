n, m = map(int, input().split())
num_arr = list(map(int, input().split()))
checked = [False] * len(num_arr)
num_arr.sort()

result_set = set()
result = [0] * m


def dfs(level):
    if level == m:
        result_set.add(tuple(result))
        return
    for i in range(len(num_arr)):
        if checked[i]:
            continue
        result[level] = num_arr[i]
        checked[i] = True
        dfs(level + 1)
        checked[i] = False


dfs(0)
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
