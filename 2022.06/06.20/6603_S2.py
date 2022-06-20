# URL : https://www.acmicpc.net/problem/6603
import itertools

while True:
    # 리스트의 첫 원소가 0이라면 케이스 종료
    arr = list(map(int, input().split()))
    result = []
    if arr[0] == 0:
        break
    # 리스트의 첫 원소는 숫자의 갯수 N, 나머지는 리스트
    else:
        n = arr[0]
        arr = arr[1:]

        c = itertools.combinations(arr, 6)

        for item in c:
            result.append(list(item))

        for i in range(len(result)):
            for val in result[i]:
                print(val, end=' ')
            if i != len(result)-1:
                print()

        print()
        print()