from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def random_position_y():
    num = random.randint(-250, 250)
    while num % 60 != 0:
        num = random.randint(-250, 250)
    return num


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_car(self):

        random_chance = random.randint(1, 4)

        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random_position_y())
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed = self.speed + 3
