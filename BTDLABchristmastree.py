def pnt_leaf(b):
   
    
    for i in range(b,0,-1):
        c = 1
        for j in range(b,i-2,-1):
            print(' '*j,end='')
            print('*'*c)
            c += 2
            
k = int(input())   
pnt_leaf(k)
print(' '*k + '|')
print('='*k +'V'+'='*k)

    

    

   

