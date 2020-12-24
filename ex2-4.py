def odd_list(al):
    # เติมส่วนของคำสั่ง
    outodd = []
    for i in al :
        if i%2 != 0 :
            outodd.append(i)
    return outodd
    
        
        
            
        
        

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
#print(ls)
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)