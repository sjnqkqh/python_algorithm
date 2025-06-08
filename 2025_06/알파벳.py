n, m = map(int, input().split())
arr = []
vector = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for _ in range(n):
    arr.append(list(input()))
result = [0]
cache = set()


def dfs(now_i: int, now_j: int, bitmask: int, max_cnt: int):
    result[0] = max(result[0], max_cnt)
    cache.add((now_i, now_j, bitmask))
    for move in vector:
        next_i, next_j = now_i + move[0], now_j + move[1]

        if 0 <= next_i < n and 0 <= next_j < m:
            alphabet_bit = 1 << (ord(arr[next_i][next_j]) - 65)
            next_bit = bitmask + alphabet_bit
            if (next_i, next_j, next_bit) not in cache and not bitmask & alphabet_bit:
                dfs(next_i, next_j, next_bit, max_cnt + 1)


dfs(0, 0, 1 << (ord(arr[0][0]) - 65), 1)
print(result[0])
