#alphabet pattern
def pattern(n):
    a=65
    for i in range(0,n):
        ch=chr(a)
        a+=1
        for j in range(0,i+1):
            print(ch,end=' ')
        print('')
    b=64+n
    for k in range(n,0,-1):
        cl=chr(b)
        b=b-1
        for j in range(k,0,-1):
            print(cl,end=' ')
        print('')
        
pattern(7)

















