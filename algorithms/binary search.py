lis=[1,2,3,4,5,6,7,8,9]
val=int(input('enter'))
first=0
second=len(lis)-1
while first<=second:
    mid=(first+second)//2
    if lis[mid]== val:
        print('got value at',mid)
        break
    elif lis[mid]<val:
        first=mid+1
    else:
        second=mid-1
else:
    print('not found')
    
    
    


