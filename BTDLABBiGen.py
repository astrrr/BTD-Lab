k = int(input())
result = 2**k
list_result = []

for i in range(result) :
    temp = bin(i)[2:]
    while (len(temp) != k) :
        temp = '0'+temp

    list_result.append(temp)



print('[',end='')
for j in list_result:
    print(j,sep=', ',end='')
    if j != list_result[-1]:
        print(", ",end='')

print(']')

