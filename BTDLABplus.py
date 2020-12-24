k = input()
opr = []
num = []

for i in k.split("+") :
    num.append(int(i))
    opr.append("+")
    

print(num)
num.sort(reverse=True)
print('*******************')
print(num)
#while len(num) != 0:
#    print(num.pop(),end='')
#    if len(num) != 0 :
#        print(opr.pop(),end='')