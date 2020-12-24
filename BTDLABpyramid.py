v = int(input())
k = 0
for i in range(v):
    for j in range((v-2),-1,-1):
        print(' ',end='')
    v-= 1    
    print('*'*((i+1)+k))
    k += 1

for i in range((k-2),-1,-1):
    for j in range(v+1):
        print(' ',end='')
    v+=1
    k -= 1
    print('*'*(i+k))

