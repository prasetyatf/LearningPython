class hero:#ini adalah template
    tes = 0#ini adalah contoh class variable

    #__init__ adl salah satu magic keyword
    def __init__(self, IniName, IniPower):#__init__ adalah instance pertama yang dipanggil dalam class hero
        #dibawah ini adalah instance variable
        self.name = IniName#ini adl template alu.name atau zilong.name
        self.power = IniPower
    
    def serang(self, lawan):
        print(f'{self.name} menyerang {lawan.name}')
        
alu = hero("alu", 200)#ini adalah object/instance
zilong = hero("zilong", 100)#ini adalah object/instance

alu.serang(zilong)#ini adalah method dengan argumen
print(alu.serang)
print(alu.__dict__)#__dict__ dapat menampilkan semua atribut