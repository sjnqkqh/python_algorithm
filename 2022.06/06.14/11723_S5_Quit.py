# URL : https://www.acmicpc.net/problem/11723

n = int(input())
dataSet = set()

for _ in range(n):
    inputData = input().split()
    order = str(inputData[0])
    number = int(inputData[1]) if order != "all" and order != "empty" else 0

    if order == "add":
        dataSet.add(number)
    elif order == "remove":
        if number in dataSet:
            dataSet.remove(number)
    elif order == "check":
        if number in dataSet:
            print(1)
        else:
            print(0)
    elif order == "toggle":
        if number in dataSet:
            dataSet.remove(number)
        else:
            dataSet.add(number)
    elif order == "all":
        dataSet = set({i for i in range(1, 21)})
    else:
        dataSet.clear()
