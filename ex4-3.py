class Stack :
    #Author Sekson123
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

result = Stack()
operate = Stack()
print(' ***Postfix expression calcuation***')
k = input('Enter Postfix expression : ')
i = 0
for i in k.split() :
    
        if i != '+' and i != '-' and i != '*' and i != '/' :
            result.push(i)
            #print(result.items)
        else :
            if i == '+' :
                if result.size() > 1 :
                
                
                    operate.push(result.pop())
                    operate.push(result.pop())
                    result.push((float(operate.items[-1])) + (float(operate.items[-2])))
                    while len(operate.items) != 0 :
                        operate.pop()

            elif i == '-' :
                if result.size() > 1 :
                    
                
                    operate.push(result.pop())
                    operate.push(result.pop())
                    result.push((float(operate.items[-1])) - (float(operate.items[-2])))
                    while len(operate.items) != 0 :
                        operate.pop()

            elif i == '*' :
                if result.size() > 1 :
                    
                    operate.push(result.pop())
                    operate.push(result.pop())
                    result.push(float(operate.items[-1]) * float(operate.items[-2]))
                    while len(operate.items) != 0 :
                        operate.pop()

            elif i == '/' :
                if result.size() > 1 :
                    
                    operate.push(result.pop())
                    operate.push(result.pop())
                    result.push(float(operate.items[-1]) / float(operate.items[-2]))
                    while len(operate.items) != 0 :
                        operate.pop()


    

print('Answer :  %.2f'%(result.pop()))
#print(result.items)
#print(k)
'''print(k[-1])
print(k[-2])
print(k[-3])'''
#print(k.split())