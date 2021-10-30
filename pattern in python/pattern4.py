# inverse pyramid
def pattern(n):
    k = n*2
    for i in range(0,n):
        for j in range(0,k):
            print(end=' ')
        k=k-2
        for j in range(0,i+1):
            print('*',end=' ')
        print('\n')
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=' ')
        k=k+2
        for j in range(0,i+1):
            print('*',end=' ')
        print('\n')          
pattern(6)
