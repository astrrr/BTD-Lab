k = int(input('enter number : '))
#check
hrm = []
result = 0
for i in range(1,k):
    if k%i == 0 :
        hrm.append(i)

for a in hrm :
    result += a
print(result)

if result == k :
    print('This number is a perfect number !!')
else :
    print('Sorry ,This number is not a perfect number !')
