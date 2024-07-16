n = int(input())
arr = list(map(int, input().split()))
reverse_arr = arr[::-1]  # 감소하는 수열 탐색용

increase_dp = [1] * n
decrease_dp = [1] * n

for i in range(1, n):
    for j in range(i):
        # 0~(1...N)까지 범위에서 증가하는 수열과 감소하는 수열의 크기를 저장
        if arr[i] > arr[j]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)
        if reverse_arr[i] > reverse_arr[j]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + 1)

decrease_dp.reverse()  # 반대로 뒤집은 배열(reverse_arr)을 기준으로 증가하는 수열의 길이를 저장했기에 다시 반전

result = -1
for i in range(n):
    # 특정 시점 i에서 최대가 되는 증가하는 수열의 길이 탐색 (증가하는 수열의 길이 + 감소하는 수열의 길이 - 1(두 수열의 가장 큰 값은 중복되기 때문에))
    result = max(result, increase_dp[i] + decrease_dp[i] - 1)

print(result)
