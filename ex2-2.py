print(' *** Wind classification ***')
wind =float( input('Enter wind speed (km/h) : '))
if wind >= 0 and wind <= 51.99 :
    print('Wind classification is Breeze.')
elif wind >= 52.00 and wind <= 55.99 :
    print('Wind classification is Depression.')
elif wind >= 56.00 and wind <= 101.99 :
    print('Wind classification is Tropical Storm.')
elif wind >= 102.00 and wind <= 208.99 :
    print('Wind classification is Typhoon.')
elif wind >= 209.00 :
    print('Wind classification is Super Typhoon.')