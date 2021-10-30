#single inheritence
class parent:
    def func1(self):
        print('it is func1')
class child(parent):
    def func2(self):
        print('it is func2')
chi=child()
chi.func2()
chi.func1()

