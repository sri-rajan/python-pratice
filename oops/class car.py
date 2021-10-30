class car():
    def __init__(self,model,year,price):
        self.model=model
        self.year=year
        self.price=price
    def incmoney(self):
        self.price=self.price*2
honda=car('city',2015,100)
tata=car('bolt',2014,200)
print(honda.year)
print(honda.__dict__)
honda.incmoney()
print(honda.price)


#insted of defining each value class is used
"""
honda=car()
tata=car()
honda.model='city'
honda.year=2012
honda.price=10000

tata.model='bolt'
tata.year=2014
tata.price=20000
print(honda.price)
"""
