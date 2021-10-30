class car():
    def __init__(self,model,year,price):
        self.model=model
        self.year=year
        self.price=price
    def incmoney(self):
        self.price=self.price*2


class supercar(car):
    #def __init__(self,model,year,price):
    pass
       # supercar.__init__(model,year,price)
honda=supercar('city',2015,100)
tata=car('bolt',2014,200)
honda.cc=150
print(honda.cc)
print(honda.year)
print(honda.__dict__)
print(tata.__dict__)
#print(help(honda))
honda.incmoney()
print(honda.price)   
