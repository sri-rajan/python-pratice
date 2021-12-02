'''
Hackerrank link:

https://www.hackerrank.com/challenges/capitalize/problem

To capitalize a name 

example

sri rajan => Sri Rajan
&
sri 12rajan dude => Sri 12rajan Dude

'''

def solve(s):
    val = s.split(" ")
    return " ".join(words.capitalize() for words in val)
result = solve("1sri rajan rana")
print(result)
