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

print(' ***Decimal to Binary use Stack***')
k = int(input('Enter decimal number : '))
result = Stack()
while k != 0 :
    if k % 2 == 1:
        result.push('1')
        k = k//2    
    else:
        result.push('0')
        k = k/2
print('Binary number : ',end='')
for i in result.items[ : : -1 ] :
    print(i,end='')
