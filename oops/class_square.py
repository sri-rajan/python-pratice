class square:
    def __init__(self,side):
        self._side=side
    @property    
    def side(self):
        return self._side
    @side.setter
    def side(self,value):
        if value>=0:
            self._side=value
        else:
            print('error')
    @classmethod
    def unit_square(cls):
        return cls(1)
    @property         
    def area(self):
        return self._side **2
s=square(6)
print(s.side)
print(s.area)









        
