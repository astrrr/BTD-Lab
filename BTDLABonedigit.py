num = input()
j = 0
while len(str(num)) != 1 :
      result = []
      for i in str(num) :
            j = int(i)
           result.append(j)
      result = sum(result)
      num = result

print(num)