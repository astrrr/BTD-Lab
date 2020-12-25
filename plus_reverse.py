a = int(input())
b = int(input())

c = str(a+b)
result = [] 
for i in c:
    result.append(i)

result.reverse()
print(*result,sep='')