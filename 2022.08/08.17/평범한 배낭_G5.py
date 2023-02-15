from collections import deque

N, K = map(int, input().split())
arr = []
dp_dict = dict({0: 0})
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort()
item_queue = deque(arr)

while item_queue:
    item = item_queue.popleft()
    keys = sorted(list(dp_dict.keys()), reverse=True)
    keys.append(0)

    for key in keys:
        if key + item[0] <= K:
            if dp_dict.get(key + item[0]) is None:
                dp_dict[key + item[0]] = dp_dict[key] + item[1]
            else:
                dp_dict[key + item[0]] = max(
                    dp_dict[key + item[0]], dp_dict[key] + item[1]
                )

result = sorted(list(dp_dict.items()), key=lambda x: x[1], reverse=True)
print(0 if len(result) == 0 else result[0][1])
