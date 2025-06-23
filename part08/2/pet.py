class Pet:
    def __init__(self,name,species,yearOfBirth):
        self.name = name
        self.species = species
        self.yearOfBirth = yearOfBirth

def new_pet(name: str, species: str, yearOfBirth: int):
    pet = Pet(name,species,yearOfBirth)
    return pet

fluffy = new_pet("Fluffy", "dog", 2017)
print(fluffy.name)
print(fluffy.species)
print(fluffy.yearOfBirth)