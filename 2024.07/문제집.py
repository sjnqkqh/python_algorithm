import heapq

n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(map(int, input().split()))

nums = {}
for i in range(1, n + 1):
    nums[i] = i

for a, b in arr:
    nums[a] = nums[b]
    nums[b] = nums[a] + 1

l = list(nums.items())
result_dict = {}
for k, v in l:
    if result_dict.get(v) is None:
        result_dict[v] = [k]
    else:
        heapq.heappush(result_dict[v], k)

sorted_arrays = list(result_dict.items())
sorted_arrays.sort()

result = []
for item in sorted_arrays:
    result = result + item[1]

print(result)
