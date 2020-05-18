import math
from price import price
from change import change
print('Change :', change)
change=change%1
change=change*100
if change%25 !=0:
    quaters=change//25
    balance=change%25
    print('Quaters :', quaters)
    if balance != 0:
        dime= balance//10
        print('Dime :', dime)
        balance = change % 10
        if balance != 0:
            nickel= balance//5
            print('Nickel :', nickel)
            balance=change % 5
            if balance != 0:
                cent= balance
                print('Cent :',cent.__round__())


else:
    if change/75 ==1 :
        print('Quater X 3')
    elif change/50 == 1 :
        print('Quater X 2')
    elif change/25 == 1:
        print('Quater X 1')








