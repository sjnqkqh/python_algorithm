import math

n = int(input())
# string = list(str(int(math.factorial(n))))
# string.reverse()
#
# for i in range(len(string)):
#     if string[i] != '0':
#         print(i)
#         break
print(n // 5 + n//5**2 + n // 5**3)
