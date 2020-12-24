class Stack :
    #Author Sekson123 v6
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else :
            self.items = list

    def push(self,i):
        self.items.append(i)
            

    def pop(self):
        if self.size() != 0 :
            return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

print(' ***Infix to Postfix***')
k = input('Enter Infix expression : ')
print('PostFix : ')

operation = Stack()
temp = Stack()
hiPriority = ['*','/']
loPriority = ['+','-']
bracket = ['(',')']

for i in k :
    temp.push(i)

for j in temp.items :
    if j != '+' and j != '-' and j != '*' and j != '/' and j != '(' and j != ')' :
        print(j,end='')

    else :
        if operation.size() > 0 :
            if j in hiPriority :
                if operation.peek() in loPriority  :
                    operation.push(j)
                elif operation.peek() in hiPriority :
                    print(operation.pop(),end='')
                    operation.push(j)
                elif operation.peek() == ')' :
                        if len(operation.items) > 1 :
                            operation.pop()
                            print(operation.pop(),end='')
                            operation.push(j)
                        else :
                            operation.push(j)
                elif operation.peek() == '(' :
                        operation.pop()
                        operation.push(j)
                        
                        



            elif j in loPriority :
                    if operation.peek() in '(' :
                        operation.pop()
                        operation.push(j)
                    
                    elif operation.peek() in hiPriority :
                        if  len(operation.items) > 1 :
                            print(operation.pop(),end='')
                            print(operation.pop(),end='')
                            operation.push(j) 
                        else :
                            print(operation.pop(),end='')
                            operation.push(j)

                    elif operation.peek() in ')' :
                        if len(operation.items) > 1 :
                            operation.pop()
                            print(operation.pop(),end='')
                            operation.push(j)
                        else :
                            operation.pop()
                            operation.push(j)
                        
                    elif operation.peek() in loPriority :
                        print(operation.pop(),end='')
                        operation.push(j)    

                    

            elif j in '(' :
                operation.push(j)
            elif j in ')':
                if operation.peek() in '(' :
                    operation.pop()
                elif operation.peek() in loPriority :
                    
                    operation.push(j)
                elif operation.peek() in hiPriority :
                    print(operation.pop(),end='')
                    #operation.pop()
                    #operation.push(j)
                    
        else:        
             operation.push(j)      

        
        
                
while '(' in operation.items :
    operation.items.remove('(')
while ')' in operation.items :
    operation.items.remove(')')

while len(operation.items) != 0 :

    print(operation.pop(),end='')

