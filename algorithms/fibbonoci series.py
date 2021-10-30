a=int(input('no of terms'))
first=0
second=1
count=0
if a<=0:
    print('type positive no')
elif a==1:
    print(first)
else:
    print('fibbonoci series is')
    while a > count :
        print(first)
        third=first+second
        first=second
        second=third
        count += 1
        
    
    
    
