from collections import deque
from collections import Counter

# data = deque([2,3,4])
# data.appendleft(1)
# data.append(5)
#
# print(data)
# print(list(data))

counter = Counter(["red", "blue", "red", "green", "blue", "blue"])

print(counter["blue"])
print(counter["red"])
print(counter)
print(dict(counter))
print(list(counter))
