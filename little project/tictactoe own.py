# dictionary for board

pl={"7":" ","8":" ","9":" ",
           "4":" ","5":" ","6":" ",
           "1":" ","2":" ","3":" "}

#initial layout of game
print("demo for game")
print("7"+"|"+"8"+"|"+"9")
print("-+-+-")
print("4"+"|"+"5"+"|"+"6")
print("-+-+-")
print("1"+"|"+"2"+"|"+"3")
print("____________________________")

# print the display of game
print("games start")

def gameprint(pl):
    print(pl["7"]+"|"+pl["8"]+"|"+pl["9"])
    print("-+-+-")
    print(pl["4"]+"|"+pl["5"]+"|"+pl["6"])
    print("-+-+-")
    print(pl["1"]+"|"+pl["2"]+"|"+pl["3"])

#game program
def game():
    count=0
    turn="X"
    na1=input("player no 1")
    na2=input("player no 2")
    players={"X":na1,"O":na2}
    for i in range(9):
        gameprint(pl)
        
        player=input("enter the place player "+turn)
        if pl[player]!=" ":
            print("already filled enter another place")
            continue
        else:
            pl[player]=turn
            count +=1

        #game logic
        if count >=5:
            if pl["7"]==pl["8"]==pl["9"]!=" " or pl["4"]==pl["5"]==pl["6"]!=" " or pl["1"]==pl["2"]==pl["3"]!=" ":
                print("***** you win *** "+players[turn])
                break
            elif pl["7"]==pl["5"]==pl["3"]!=" " or pl["1"]==pl["5"]==pl["9"]!=" ":
                print("**** you win **** "+players[turn])
                break
            elif pl["3"]==pl["6"]==pl["9"]!=" " or pl["2"]==pl["5"]==pl["8"]!=" " or pl["1"]==pl["4"]==pl["7"]!=" ":
                print("**** you win **** "+players[turn])

        # if it is tie
        if count==9:
            print("*** its tie ***")

            
        #changing the turns
        if turn=="X":
            turn="O"
        else:
            turn="X"

    # asking again to play
    choice=input("do you want to play again (y or n)")
    if choice=="y" or "Y":
        for ke in pl.keys():
            pl[ke]=" "
        game()
        
game()





























