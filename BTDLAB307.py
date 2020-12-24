lap = int(input())
sentence = []
check = False
for i in range(lap):
   sentence.append(input())

print(sentence[0],end=' ')
for j in sentence[1].split() :
    if j == sentence[0].split()[-1] :
        check = True
    
    elif check == True:
        print(j,end=' ')
        