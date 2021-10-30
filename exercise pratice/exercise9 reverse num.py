def if_orginal(a):
    orginalNum = a
    reverseNum = 0
    while (a > 0):
        reminder = a % 10
        reverseNum = (reverseNum * 10) + reminder
        a = a//10
    if (orginalNum == reverseNum):
        print('true')
    else :
        print('false')
if_orginal(121)
if_orginal(122)
  
    
    
    











              
