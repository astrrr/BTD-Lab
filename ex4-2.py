class Stack :
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else :
            self.items = list

    def push(self,i):
        self.items.append(i)
            

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []
    
    def delete(self,i):
        return self.items.remove(i)

def match(open, close): 
    return (open == '(' and close == ')') or  (open == '{' and close == '}') or (open == '[' and close == ']') 

def parenMatching(str): 
    s = Stack()
    s1 = Stack()
    s2 = Stack() 
    i= 0  
    error = 0

    while i < len(str)   : 
        c = str[i]
        
        
        if c in'{[(' : 
            s.push(c)
            s1.push(c) 
            
        else: 
            if c in'}])':
                s2.push(c) 
                if s.size() > 0 and s2.size() > 0: 
                        if not match(s.pop(), s2.pop())  : 
                            error = 1 
                        else:
                            if s1.size() > 0 and s2.size() > 0 :
                                if not match(s1.items[-1], s2.items[0]) :
                                    error = 1
                                else :
                                    error = 2
                                 
        i+= 1

    if s.size() > 0 and error ==0  :  
        error = 3
    elif s.size() == 0 and s2.size() >0 and error ==0 :
        error = 2 
    #elif s2.size() > 0  and error ==0:
     #   error = 2
    elif s.size()> 0 and s2.size() ==0 and error ==0:
        error = 3
    elif s1.size() > 0 and s2.size() > 0 and error ==0:
         if not match(s1.items[-1], s2.items[0]) :
             error = 1


    return error,c,i,s,s1,s2



str= input('Enter expresion : ') 
err,c,i,s,s1,s2 = parenMatching(str)
if err == 1: 
    print(str, 'Unmatch open-close  ')
elif err == 2 : 
    print(str, 'close paren excess') 
elif err == 3: 
    print(str, 'open paren excess  ', s.size(),': ',end=''  )
    for ele in s.items : 
         print(ele,sep=' ',end = '') 
    print() 
else: 
    print(str, 'MATCH')
#print(err)
#print(c)
#print(i)
#print(s.items)
#print(s1.items)
#print(s2.items)
#print(match(s1.items[0],s2.items[-1]))