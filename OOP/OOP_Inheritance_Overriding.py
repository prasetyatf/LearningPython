# Overriding. I've learned from many sources. especially from abook named "Python Basic A Self-Teachimg Introduction"
# these codes are not in the book, but i write these codes

class Abc:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'nama saya adalah {self.name}')

class Xyz(Abc):

    def __init__(self, name):
        super().__init__(name)
        self.umur = 25

    def show(self):
        print(f'nama saya adalah {self.name} dan berumur {self.umur}')

tegar = Abc('Tegar')
pras = Xyz('pras')
tegar.show()
pras.show() #Overriding. same name, different task with inheritance
# while Overloading is similiarly Overriding but without inheritance
# https://www.geeksforgeeks.org/difference-between-method-overloading-and-method-overriding-in-python/