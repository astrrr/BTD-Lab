k = input()

for i in k:
    if i.islower() :
        print(i.upper(),end='')
    elif i.isupper() :
        print(i.lower(),end='')
    else:
        print(i,end='')

