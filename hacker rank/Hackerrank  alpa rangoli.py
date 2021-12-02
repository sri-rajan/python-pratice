'''
Hackerrank link:

https://www.hackerrank.com/challenges/alphabet-rangoli/problem

to print a rangoli like alpabets
example:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

'''

import string 
alpha= string.ascii_uppercase # this is noting but a alpabets  ..abcdefghijklmnopqrstuvwxyzs

def print_rangoli(size):
    width = (4*size) -3
    count = list(range(size)[::-1]) + list(range(1,size))
    for i in count:
        print('-'.join(alpha[size-1:i:-1] +alpha[i:size]).center(width, '-'))
print_rangoli(5)
print(alpha)
print(alph)
print(alpha == alph)
    
