def pattern(n):
    k=1
    a=n+(n-1)
    for i in range(0,n):
        for i in range(0,k):
            print(end=' ')
        k=k+2
        for j in range(a,0,-1):
            print('*',end=' ')
        a=a-2
        print('')
pattern(8)
            









