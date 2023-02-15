N = int(input())
arr = list(map(int, input().split()))

result = 0
highest = -1


def solve(sum: int, highest, step):
    global result
    result = max(result, sum)
    if step == N:
        return

    if highest < arr[step]:
        solve(sum + arr[step], arr[step], step + 1)  # 해당 노드를 더한 값 -> 최댓값 증가
        solve(sum, highest, step + 1)  # 해당 노드를 더하지 않은 값 -> 최댓값 유지
    else:
        solve(sum, highest, step + 1)  # 해당 노드를 더하지 않은 값 -> 최댓값 유지


solve(0, 0, 0)
print(result)
