class ManusiaBiasa:

    def __init__(self, name, gender):
        self.nama = name
        self.gender = gender
    
    def enhanced_attack(self): # object method. hanya melekat pada object
        return 'enhanced attack activated'
    
    @classmethod
    def attack(cls): # class method. dapat melekat pada object dan class. can access or modifi class
        return 'attack!'
    
    @staticmethod # class method. dapat melekat pada object dan class. can't access or modifi class
    def move():
        return 'moving..'

ahri = ManusiaBiasa('ahri', 'girl')
# darius = ManusiaBiasa.enhanced_attack() akan error
darius = ManusiaBiasa.attack()
yasuo = ManusiaBiasa.move()

print(ahri)
print(ahri.attack())
print(darius)
print(yasuo)
