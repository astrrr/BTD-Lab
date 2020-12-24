lap = int(input())
sentence = []
last = []
check = False
for i in range(lap):
   sentence.append(input())

#มีประโยคทั้งหมดแล้ว

#check หัวท้าย
for i in range(lap):

    
    if (i+1 <= len(sentence)):  
        for j in range(len(sentence[i].split()),-1,-1):
            print(sentence[i].split()[j])