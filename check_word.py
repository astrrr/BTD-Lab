s1 = input()
s2 = input()[:-1]
count1,count2,a=0,0,[]
for i in s1:
  count1 +=1
for i in s2:
  count2 += 1
a.append(count1)
a.append(count2)
print(max(a))
print(min(a))