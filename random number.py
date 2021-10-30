import random
n=30
game_value=int(n*random.random())+1
count=0
while count != game_value:
    count=int(input('number'))
    if count>0:
        if count < game_value :
            print('small')
        elif count > game_value:
            print('big')
    else:
        print('give up')
        break
else :
    print('you win')
        
    
