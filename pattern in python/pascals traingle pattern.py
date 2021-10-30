def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(function(i,j),' ',end='')
        print('')
def function(n,k):
    a=1
    if k>n-k:
        k=n-k
    for i in range(0,k):
        a=a*(n-i)
        a=a//(i+1)
    return(a)
pattern(8)        
        
