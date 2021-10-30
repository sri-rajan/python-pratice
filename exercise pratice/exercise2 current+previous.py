def cps(num):
    a = 0
    for i in range(num):
        print('current num',i,'previous num',a,'sum:',i+a)
        a = i
cps(10)
    
