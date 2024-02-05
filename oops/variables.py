class car:
    wheels = 4
    def __init__(self):
        self.name = "tata"
        self.milage = "17"

car1 = car()
car2 = car()
car.wheels = 6
car2.milage = 19
print(car1.name, car1.milage, car1.wheels)
print(car2.name, car2.milage, car2.wheels)