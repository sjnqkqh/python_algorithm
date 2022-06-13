# Page 113

max_hour = 5
result = 0

for hour in range(max_hour+1):
    for minute in range(60):
        for second in range(60):
            time = str(hour) + str(minute) + str(second)
            if time.__contains__("3"):
                result = result + 1

print(result)