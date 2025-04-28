true = True
false = False

class Person:
    def __init__(self, name, house, age, isFem, culture, faith, title=[],dna=None, father=None, mother=None):
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
        

        if self.isFem == False:
            self.gen = "male"
        else:
            self.gen = "female"
    def __str__(self):
        return 
    
class Culture:
    def __init__(self,orgin,nation=""):
        self.orgin = orgin
        self.nation = nation
    def __str__(self):
        if self.nation=="":
            return f"{self.orgin}"
        else:
            return f"{self.orgin} {self.nation}"
    
class Faith:
    def __init__(self,rel,faith=""):
        self.rel = rel
        self.faith = faith
    def __str__(self):
        if self.faith=="":
            return f"{self.rel}"
        else:
            return f"{self.faith} {self.rel}"
    

germam = Culture("German","American")

christian = Faith("Christianity")

p1 = Person("Clark",14,False,germam,christian)