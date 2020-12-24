k = input()

in_list = k.split(",")
result = []
for i in in_list:
    if i == '1':
        result.append(i)
    elif( int(i)%7 == 0 and int(i)%11 != 0):
        result.append(i)

print(*result, sep=',')