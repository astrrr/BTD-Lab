def sum_num(number):
    temp = 0
    for i in number:
        temp += int(i)
    return list(str(temp))

k = list(str(input()))

#บวกทุกตัวจนกว่าจะเหลือหลักเดียว
while len(k) > 1:
    
    k = sum_num(k)

print(*k)