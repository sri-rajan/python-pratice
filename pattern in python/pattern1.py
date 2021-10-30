def pattern(n):
    k=n*2-2
    for i in range(0,n):
        for j in range(k,0,-1):
            print(end=" ")
        k=k-1
        for j in range(0,i):
            print('*',end=' ')
        print('\r')
pattern(7)
