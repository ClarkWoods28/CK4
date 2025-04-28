true = True
false = False

class Nation:
    def __init__(self, name, gov, ruler, culture=None, faith=None):
        self.name = name
        self.gov = gov
        self.ruler = ruler

        self.jobs = {}
        self.laws = {}
        self.history = {}

    def __str__(self):
        return self.name

class Person:
    def __init__(self, name, house, age, isFem, culture, faith, dna=None, father=None, mother=None, title=[]):
        self.name = name
        self.house = house
        self.age = age
        self.isFem = isFem
        self.culture = culture
        self.faith = faith
        self.title = title
        self.dna = dna
        self.father = father
        self.mother = mother

        self.location = 0
        self.courtLoc = None 
        self.history = {}
        self.traits = []
        self.modifiers = []
        

        if self.isFem == False:
            self.gen = "male"
        else:
            self.gen = "female"
    def __str__(self):
        return self.name + self.house
    
class Culture:
    def __init__(self,name,herit):
        self.name = name
        self.herit = herit
    def __str__(self):
        return self.name
    
class Faith:
    def __init__(self,name,rel):
        self.name = name
        self.rel = rel
    def __str__(self):
        return self.name
    

germam = Culture("German","American")

christian = Faith("Christianity")

p1 = Person("Clark",14,False,germam,christian)
