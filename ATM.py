k = input()
k.split()


num = ['0','1','2','3','4','5','6','7','8','9']
result_list = []
temp =''
for i in k:
    if i in num :
        temp += i

    else :
        if temp != '' :
            result_list.append(temp)
            temp = ''

result = 0
for i in result_list:
    result += int(i)


print(str(result).zfill(4))