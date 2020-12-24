print(' *** Summation of each digit ***')
k1 = input('Enter a positive number : ')
k2 = 0
#if len(k1) < 10 :
for i in k1 :
        k2 = k2 + int(i)
print('Summation of each digit =  {}'.format(k2))
#else:
#    print('Please enter 9 digit')