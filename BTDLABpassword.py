k = input()
upper = []
lower = []
number = []
sign = []

if 3 <= len(k) <= 20 :
    for i in k :
        if  97 <= ord(i)  <= 122:
            lower.append(i)

        elif 65 <= ord(i) <= 90:
            upper.append(i)

        elif 48 <= ord(i) <= 57:
            number.append(i)

        else:
            sign.append(i)

    if len(upper)>=1 and len(lower)>=1 and len(number)>=1 and len(sign)>=1 :
        print('Valid')

    else:
        print('Invalid')

else:
    print('Invalid')