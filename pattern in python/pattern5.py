# inverse
def pattern(n):
    k=n-2
    for i in range(n,0,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for j in range(i,0,-1):
            print('* ',end='')
        print('\r')
#straight
    k=2*n-3
    for i in range(0,n):
        for j in range(0,k):
            print(end=' ')
        k=k-1
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
pattern(8)







        

























