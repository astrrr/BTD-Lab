k = input()
n = int(k.split()[0])
m = int(k.split()[1])
y = int(k.split()[2])
check = True
result = []
#A > B 
lap = 0

B = 1
A = B*m
y_a = y- n
y_b = y

while check == True:
    
    #เพิ่มA และ B เป็นจำนวน n เท่าจนกว่า A > B จริง
    if ((A+y_a)==(B+y_b)):
        #ปัจจุบัน A-n เท่า B
        if((A-n) == (B)):
            result.append(A+y)
            result.append(B+y)
            check = False
    elif lap > 50000:
        print('Timeout.')
        check = False
    B *=n
    A *=n
    lap += 1

print(*result)