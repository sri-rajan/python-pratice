class parent:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def view(self):
        print(self.name,self.age)
class child(parent):
    def __init__(self,name,age,lname):
        parent.__init__(self,name,age)
        self.lname=lname
        self.good="is good"
    def view(self):
        print(self.name,self.lname,self.good,self.age)
ob=child("python",23,"programming")
ob.view()
