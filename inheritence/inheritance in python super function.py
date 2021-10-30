#super function   -calls a parent method directly
class parent:
    def func1(self):
        print('it is func1')
class child(parent):
    def func2(self):
        super().func1()
        print('it is func2')
chi=child()
chi.func2()

