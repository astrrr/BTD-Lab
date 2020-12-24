num = input()

while len(num) != 1 :
      temp = 0  
      for i in num :
            temp = temp+int(i)
      num = str(temp)
      
print(num)