#method overriding function   -calls a parent method directly
class parent:
    def func1(self):
        print('it is func1')
class child(parent):
    def func1(self):
        print('it is func2')
chi=child()
chi.func1()

