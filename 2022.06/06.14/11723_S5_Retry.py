# URL : https://www.acmicpc.net/problem/11723
import sys

n = int(input())
arr = [False for _ in range(21)]  # 선형 접근이 가능하도록

for _ in range(n):
    inputData = sys.stdin.readline().rstrip().split()
    order = str(inputData[0])
    number = int(inputData[1]) if order != "all" and order != "empty" else 0

    if order == "add":
        arr[number] = True
    elif order == "remove":
        arr[number] = False
    elif order == "check":
        print(int(arr[number]))
    elif order == "toggle":
        arr[number] = False if arr[number] else True
    elif order == "all":
        arr = [True for _ in range(21)]
    else:
        arr = [False for _ in range(21)]
