'''
Hackerrank link:

https://www.hackerrank.com/challenges/the-minion-game/problem

detail:

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

get +1 point for each occurrence of the substring in the string S.

example:
string = BANANA
kevin's vowel beginning word = ANA
here, ANA occurs twice in BANANA. hence, kevin will get 2 points

diagram example:

https://s3.amazonaws.com/hr-challenge-images/9693/1450330231-04db904008-banana.png

'''


def minion_game(s):
    vowels = 'AEIOU'

    kevin_score = 0
    stuart_score = 0
    size = len(s)
    for i in range(size):
        if s[i] in vowels:
            kevin_score += (size-i)
        else:
            stuart_score += (size-i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print ("Stuart", stuart_score)
    else:
        print("Draw")

minion_game("BANANA")






