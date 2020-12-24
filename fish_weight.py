list_A = []
k = int(input())
while (k !=0 ):
    list_A.append(k)
    k = int(input())
    

j = input()

if j.lower() == 'max':
      list_A.sort(reverse=True)
      print(*list_A)

elif j.lower() == 'min' :
      list_A.sort()
      print(*list_A)
            