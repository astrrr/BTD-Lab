k = input()
k.split()
upper = 0
lower = 0

for i in k:
    if (i.isupper() == True):
        upper += 1
    
    elif (i.islower() == True):
        lower += 1

print("UPPER:",end='')
print(upper)
print("LOWER:",end='')
print(lower)