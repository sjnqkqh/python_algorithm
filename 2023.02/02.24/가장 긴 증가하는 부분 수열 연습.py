import bisect

arr = [0,3,5,7,9,2,1,4,8]
n = len(arr)-1


def method_1_n_square():
    increase = [1] * n
    for i in range(1, n):
        for j in range(n):
            if arr[i] > arr[j]:
                increase[i] = max(increase[i], increase[j] + 1)

    return increase


def method_2_n_log_n():
    increase = [arr[0]]
    for i in range(n):
        if arr[i] > increase[-1]:
            increase.append(arr[i])
        else:
            a = bisect.bisect_left(increase, arr[i])
            increase[a] = arr[i]

    return increase

