# Inheritance. jagongoding.com

class Orang:

    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
        print('fungsi Orang.__init__ dieksekusi')
    
    def perkenalan(self):
        print(f'Perkenalkan, nama saya {self.nama} dari {self.asal}')

class pekerja(Orang):
    
    def __init__(self, nama, asal, hobi):
        super().__init__(nama, asal)
        self.hobi = hobi

class pelajar(Orang):
    
    def __init__(self, nama, asal, suku):
        Orang.__init__(self, nama, asal)
        self.suku = suku

tegar = Orang('Tegar', 'Boyolali')
prasetya = pekerja('Prasetya', 'Indonesia', 'Ngoding')
fitriaji = pelajar('Fitrijai', 'Bumi', 'Jawa')

tegar.perkenalan()
prasetya.perkenalan()
print(f'dan habi {prasetya.nama} adalah {prasetya.hobi}')
fitriaji.perkenalan()
print(f'dan suku {fitriaji.nama} adalah {fitriaji.suku}')