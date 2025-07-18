
class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.total_weigh_ins = 0

class BabyCentre:
    def __init__(self):
        self.total_weigh_ins = 0
    def weigh(self,person: Person):
        self.weight = person.weight
        person.total_weigh_ins += 1
        self.total_weigh_ins = person.total_weigh_ins
        return self.weight
    def feed(self, person: Person):
        person.weight += 1
    def weigh_ins(self):
        return self.total_weigh_ins

        
        
        
    
baby_centre = BabyCentre()

eric = Person("Eric", 1, 110, 7)
peter = Person("Peter", 33, 176, 85)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

baby_centre.weigh(eric)
baby_centre.weigh(eric)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

baby_centre.weigh(eric)
baby_centre.weigh(eric)
baby_centre.weigh(eric)
baby_centre.weigh(eric)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")