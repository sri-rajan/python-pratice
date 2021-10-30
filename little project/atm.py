print('welcome to sri bank')
name=input('name:')
print(name,'welcome to our bank')
balance=100
chances=3
restart='y'
while chances>=0:
    pin=input('enter password')
    if pin=='1234':
        print('password is correct')
        while restart not in ('n','no','N','No'):
            print('press 1 for balance')
            print('press 2 for withdraw')
            print('press 3 for deposite')
            print('press 4 for return card')
            user=int(input('enter'))
            if user==1 :
                print('your balance is ',balance)
                restart=input('go back?')
                if restart in ('n','no','N','No'):
                    print('thank you')
                    break
            elif user==2 :
                amount=int(input('amount of withdraw'))
                print('you succesfully withdraw',amount)
                balance=balance-amount
                print('your current balance is',balance)
                restart=input('go back?')
                if restart in ('n','no','N','No'):
                    print('thank you')
                    break
            elif user==3 :
                deposit=int(input('amount of deposite'))
                print('you succesfully deposite',deposit)
                balance=balance+deposit
                print('your current balance is',balance)
                restart=input('go back?')
                if restart in ('n','no','N','No'):
                    print('thank you')
                    break
            elif user==4 :
                print('thank you ')
                break
            else:
                print('correct num')
                restart='y'         
    elif pin!='1234':
        print('password is wrong')
        chances=chances-1
        if chances==o:
            print('no more tries')
            break
