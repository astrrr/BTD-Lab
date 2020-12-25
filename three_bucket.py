k = input()
raw_bucket = k.split()

color_list = ["red","green","blue","black","white","pink","orange","yellow","brown"]


in_bucket1,in_bucket2,in_bucket3= [],[],[]

for i in color_list:
    if i in raw_bucket[0]:
        in_bucket1.append(i)

    if i in raw_bucket[1]:
        in_bucket2.append(i)

    if i in raw_bucket[2]:
        in_bucket3.append(i)

result =[]

for i in in_bucket1:
    for j in in_bucket2:
        if (i==j) :
            result.append(i)

for i in result:
    if i in in_bucket3:
        result.remove(i)

if len(result) != 0:
    print(*result,sep=',')

elif len(result)==0:
    print('none')