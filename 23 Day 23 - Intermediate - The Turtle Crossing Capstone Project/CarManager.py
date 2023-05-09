from Car import Car
import random

class CarManager():

    def __init__(self):
        self.all_cars = []
        
    def create_car(self):
        chances = random.randint(1,6)
        if chances == 1:
            car = Car()
            self.all_cars.append(car)

    def move_all(self):
        for car in self.all_cars:
            car.forward(5)