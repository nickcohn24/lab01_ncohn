class Animal:
    ''' Defining an animal using species, weight, age, and name attributes '''
    def __init__(self, species=None, weight=None, age=None, name=None):
        self.weight = weight
        self.age = age
        if species != None:
            self.species = species.upper()
        else:
            self.species = species
        if name != None:
            self.name = name.upper()
        else:
            self.name = name
        
    def setSpecies(self, species):
        self.species = species.upper()

    def setWeight(self, weight):
        self.weight = weight

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = name.upper()

    def toString(self):
        print_animal = f'Species: {self.species}, Name: {self.name}, Age: {self.age}, Weight: {self.weight}'
        return print_animal

a1 = Animal("dog", 50, 10, "trix")

assert a1.name == 'TRIX'
