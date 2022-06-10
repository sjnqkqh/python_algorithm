# URL : https://www.acmicpc.net/problem/14468
import re

arr = list(input())
done = []

for i in range(len(arr)):
    start = str(arr[i]) # 문자열 시작 인덱스
    if start in done:
        continue

    end = arr.index(start, i + 1)
    print(i, end)