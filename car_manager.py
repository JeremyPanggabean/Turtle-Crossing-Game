from turtle import Turtle
import random

COLORS = [
    "navy", "maroon", "blue", "red", "purple", "brown",
    "yellow", "gray", "pink", "cyan", "violet",
    "tan", "khaki", "coral", "salmon", "crimson", "indigo",
    "turquoise", "chocolate"
]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 4


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_cars = Turtle(shape="square")
            y_post = random.randint(-250, 250)
            new_cars.shapesize(stretch_wid=1, stretch_len=2)
            new_cars.penup()
            new_cars.color(random.choice(COLORS))
            new_cars.goto(x=300, y=y_post)
            self.all_cars.append(new_cars)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT