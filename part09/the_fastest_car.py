class Car:

    def __init__(self,name: str , top_speed: int):
        self.name = name
        self.top_speed = top_speed

def fastest_car(cars: list):
    i = 0
    for car in cars:
        if i < car.top_speed:
            i = car.top_speed
    return i

if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))