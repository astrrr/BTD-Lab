k = list(str(input()))

result = []
for i in range(len(k)):
    if (i+1) % 2 == 0:
        temp = k[i].upper()
    else:
        temp = k[i].lower()
    result.append(temp)
    
print(*result,sep='')