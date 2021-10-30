#hierarchical inheritence
class parent:
    def func1(self):
        print('it is func1')
class parent2(parent):
    def func3(self):
        print('it is func3')
class child(parent):
    def func2(self):
        print('it is func2')
chi=child()
chi.func2()
chi.func1()
chi1=parent2()
chi1.func1()
