while True:
    try:
        n = int(input())

        num = 1
        while True:
            if num % n == 0:
                print(len(str(num)))
                break
            else:
                num = num * 10 + 1
    except:
        break
