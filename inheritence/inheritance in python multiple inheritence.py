#multiple inheritence
class parent:
    def func1(self):
        print('it is func1')
class parent2:
    def func3(self):
        print('it is func3')
class child(parent,parent2):
    def func2(self):
        print('it is func2')
chi=child()
chi.func2()
chi.func1()
chi.func3()
