from Animal import Animal
class AnimalShelter:
    ''' '''
    def __init__(self):
        self.shelter = {}

    def addAnimal(self, animal):
        if self.shelter.get(animal.species) == None:
            self.shelter[animal.species] = [animal]
        else:
            self.shelter[animal.species].append(animal)
        
    def removeAnimal(self, animal):
        if animal.species in self.shelter.keys():
            animal_list = self.shelter[animal.species]
            for anim in animal_list:
                if anim.name == animal.name:
                    if anim.weight == animal.weight:
                        if anim.age == animal.age:
                            self.shelter[animal.species].remove(animal)
                        else:
                            x = 'end of function string'
                    else:
                        x = 'end of function string'
                else:
                    x = 'end of function string'
        else:
            x = 'end of function string'
            
    def removeSpecies(self, species):
        if self.shelter.get(species.upper()) == None:
            x = 'end of function string'
        else:
            del self.shelter[species.upper()]
        
    def getAnimalsBySpecies(self, species):
        specie_all = ''
        specie_key = species.upper()
        if self.shelter.get(specie_key) == None:
            return ""
        else:
            counter = 0
            for animal in self.shelter[specie_key]:
                print_string = animal.toString()
                counter += 1
                if counter == len(self.shelter[specie_key]):
                    specie_all += print_string
                else:
                    specie_all += print_string + '\n'
            return specie_all
        
    def doesAnimalExist(self, animal):
        if animal.species in self.shelter.keys():
            animal_list = self.shelter[animal.species]
            for anim in animal_list:
                if anim.name == animal.name:
                    if anim.weight == animal.weight:
                        if anim.age == animal.age:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        else:
            return False



