#dont have answer now try to learn later
from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def incmoney(self):
        pass
       
class supercar(car):
    def __init__(self,model,year,price):
        super.__init__(model,year,price)
    def incmoney(self):
        self.price=self.price*2
        
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
