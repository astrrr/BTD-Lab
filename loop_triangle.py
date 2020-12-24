import math

k = int(input())
result = math.sqrt(k)
check = int(math.sqrt(k))
check_list = []


if result != check :
    print("Float")
else:
    print("Integer")