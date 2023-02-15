# URL : https://www.acmicpc.net/problem/14468

arr = list(input())
done = []
cross = []

for i in range(len(arr)):
    start = str(arr[i])  # 문자열 시작 인덱스
    if start in done:
        continue
    else:
        done.append(start)
    end = arr.index(start, i + 1)  # 두번째 문자열 인덱스

    # 두 문자열 사이에 한 번만 나타난 문자열이 있는지 확인
    for j in range(i, end):
        cow = arr[j]
        print(cow)
        find = arr.index(cow, j, end)
        print(i, end, find)
