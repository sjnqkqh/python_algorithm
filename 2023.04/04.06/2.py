INF = int(10e9)


def solution(n, s, a, b, fares):
    answer = 0

    arr = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        arr[i][i] = 0

    for item in fares:
        u, v, cost = item
        arr[u][v] = cost
        arr[v][u] = cost

    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                if arr[j][k] > arr[j][i] + arr[i][k]:
                    arr[j][k] = arr[j][i] + arr[i][k]

    answer = arr[s][a] + arr[s][b]

    for i in range(1, n + 1):
        answer = min(answer, arr[s][i] + arr[i][a] + arr[i][b])

    return answer


solution(6, 4, 6, 2,
         [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
