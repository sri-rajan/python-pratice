#to count number of time name come
#two ways of doing it
# first way___________________

a='hello man test it hello'
cout=0
for i in range(len(a)-1):
    if a[i:i+5]== 'hello':
        cout += 1
print(cout)

#second way__________________

a='hello man test it hello'
cout=0
for i in range(len(a)-1):
    cout += a[i:i+5]== 'hello'
print(cout)
   
    
    
    
    
              
