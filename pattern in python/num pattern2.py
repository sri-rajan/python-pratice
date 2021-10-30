# pascals traiangle
#nCr formula used  n!/(n-r)!r!
#binomial co-efficient
#space and time efficient binomial
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(function(i,j),' ',end='')
        print()
def function(n,k):
    res=1
    if (k>n-k):
        k=n-k
    for i in range(0,k):
        res=res*(n-i)
        res=res//(i+1)
    return (res)
pattern(8)

#1c1=1  2c2=1 --  2c0=1  3c0=1  -- 0c0=1
    





















