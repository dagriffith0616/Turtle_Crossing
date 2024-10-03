from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
X_START = 300


class CarManager:

    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.count = 0



    def create_cars(self):
        chance = random.randint(1, 6)
        if chance == 6:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(X_START, random.randint(-250, 250))
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

