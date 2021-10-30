travelling=input('travelling \n yes or no')
while travelling=='yes':
    num=int(input('number of passanger'))
    for a in range(1,num+1):
        name=input('name')
        age=input('age')
        sex=input('male or female')
        print(name)
        print(age)
        print(sex)
    travelling=input('anymore')
    

