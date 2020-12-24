import math
def isPrime(n):
    limit = int(math.sqrt(n)) +1
    for i in range(2,limit) :
        if n%i == 0 :
            return False
    return True

def showPrime(n,m):
    n = int(k.split()[0])
    m = int(k.split()[1])
    result = []
    if m < 0 or n < 0 :
        print("same or both is negative number ,Pls enter positive number")
        
    else: 
        if n >= m :
            for i in range(m,n) :
                if isPrime(i) == True :
                    result.append(i)
        else:
            for i in range(n,m) :
                if isPrime(i) == True :
                    result.append(i)
        for scan in result:
            if scan == 1 :
                result.remove(1)           
        return result

k = input("enter number : ")

p = showPrime(k.split()[0],k.split()[1])
print('prime number from '+k.split()[0] +' to ' + k.split()[1]+' : ',end='')
for i in p :
    print(i,end=' ')