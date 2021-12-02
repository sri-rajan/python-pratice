import random

def game():
    n = int(input('enter range for the game'))
    guess = 0
    ans = int(n*random.random())+1
    guess_no =0
    while ans != guess:
        guess = int(input("Enter your guess:  "))
        guess_no += 1
        if guess > 0:
            if ans == guess:
                print('your answer is right \n you take "',guess_no,'" guess'
                      ,end="\n \n \n")
            elif ans > guess:
                print('your guess is small')
            else:
                print('your guess is big')
        else:
            print("please put valid number")
while True:
    print("do you want to play the game")
    a = int(input("enter 1 or 0"))
    if a == 0:
        print("thankyou for playing the game.. bye bye..")
        break
    game()
