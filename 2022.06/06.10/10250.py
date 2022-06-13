n = int(input())

for _ in range(n):
    h, w, customer = map(int, input().split())

    if customer % h == 0:
        floor = h
        roomNumber = customer // h
    else:
        floor = customer % h
        roomNumber = customer // h + 1

    print(floor * 100 + roomNumber)
