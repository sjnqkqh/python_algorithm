def solution(triangle):
    for i in range(1, len(triangle)):
        floor = triangle[i]
        for j in range(len(floor)):
            item = floor[j]
            if j == 0:
                item = triangle[i - 1][j] + item
            elif j == len(floor) - 1:
                item = triangle[i - 1][j - 1] + item
            else:
                item = max(triangle[i - 1][j], triangle[i - 1][j - 1]) + item
            floor[j] = item

    return max(triangle[-1])


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
